// src/flutter/flet_background_service/lib/src/background_service_impl.dart
//
// FletService implementation wrapping flutter_background_service.
//
// Architecture
// ─────────────
// Python sets _command + _payload attrs then calls update().
// Flet diffs the attrs and calls our update() override.
// We read _command, decode _payload JSON, dispatch to the right handler.
// Events from the isolate come via service.on('event') and are forwarded to
// Python via control.triggerEvent('on_service_event', data).

import 'dart:convert';
import 'dart:ui';

import 'package:flet/flet.dart';
import 'package:flutter/foundation.dart';
import 'package:flutter_background_service/flutter_background_service.dart';
import 'package:flutter_local_notifications/flutter_local_notifications.dart';

// ── Top-level background isolate entry point ──────────────────────────────────
//
// @pragma('vm:entry-point') is REQUIRED. Without it the Dart compiler will
// tree-shake this function in release mode because it is not called from
// anywhere in the main isolate's call graph.
//
// This function runs in a completely SEPARATE Dart isolate. It has no access
// to Flutter widgets, BuildContext, or any state from the main isolate.
// Communication happens ONLY through ServiceInstance.invoke() / on().

@pragma('vm:entry-point')
void _onAndroidBackground(ServiceInstance service) async {
  // Required for Flutter 3.x — initialises plugin registrants in the
  // background isolate so platform channels work correctly.
  DartPluginRegistrant.ensureInitialized();

  // Tell the main isolate we are alive.
  service.invoke('event', {'type': 'service_started'});

  // ── Command listeners ───────────────────────────────────────────────────
  // The main isolate sends commands here via FlutterBackgroundService().invoke().

  service.on('stop').listen((_) {
    service.invoke('event', {'type': 'service_stopped'});
    service.stopSelf();
  });

  service.on('ping').listen((_) {
    service.invoke('event', {'type': 'pong'});
  });

  // Custom named events forwarded from Python via BackgroundService.send().
  service.on('custom').listen((Map<String, dynamic>? data) {
    if (data == null) return;
    // Re-emit so the main isolate's event listener receives it.
    service.invoke('event', {'type': 'custom', ...data});
  });

  // ── Update foreground notification ──────────────────────────────────────
  service.on('updateNotification').listen((Map<String, dynamic>? data) async {
    if (data == null) return;
    if (service is AndroidServiceInstance) {
      service.setForegroundNotificationInfo(
        title:   data['title']   as String? ?? '',
        content: data['content'] as String? ?? '',
      );
    }
  });
}

@pragma('vm:entry-point')
Future<bool> _onIosBackground(ServiceInstance service) async {
  // Called periodically by iOS BGTaskScheduler when the app is in the
  // background. Keep work minimal — iOS has a tight time budget here.
  service.invoke('event', {'type': 'service_started'});
  return true;
}

// ── FletService implementation ────────────────────────────────────────────────

class BackgroundServiceImpl extends FletService {
  final FlutterBackgroundService _svc = FlutterBackgroundService();
  bool _initialized = false;

  BackgroundServiceImpl({required super.control});

  // ── FletService lifecycle ─────────────────────────────────────────────────

  @override
  void init() {
    super.init();
    // Relay service → Python events as soon as the service object exists.
    // We subscribe here (before configure) so we never miss the first event.
    _svc.on('event').listen((Map<String, dynamic>? data) {
      if (data == null) return;
      control.triggerEvent('on_service_event', data);
    });
  }

  @override
  void update() {
    super.update();
    _dispatchCommand();
  }

  @override
  void dispose() {
    // Nothing to teardown on the Dart side — the background isolate outlives
    // the Flutter widget tree by design.
    super.dispose();
  }

  // ── Command dispatch ──────────────────────────────────────────────────────

  void _dispatchCommand() {
    final cmd = control.attrString('_command', '');
    if (cmd == null || cmd.isEmpty) return;

    final rawPayload = control.attrString('_payload', '{}') ?? '{}';
    late final Map<String, dynamic> args;
    try {
      args = json.decode(rawPayload) as Map<String, dynamic>;
    } catch (_) {
      args = {};
    }

    switch (cmd) {
      case 'initialize':
        _initialize(args);
      case 'start':
        _svc.startService();
      case 'stop':
        _svc.invoke('stop');
      case 'ping':
        _svc.invoke('ping');
      case 'send':
        _sendCustomEvent(args);
      case 'updateNotification':
        _svc.invoke('updateNotification', args);
    }
  }

  // ── Initialisation ────────────────────────────────────────────────────────

  Future<void> _initialize(Map<String, dynamic> args) async {
    if (_initialized) return;

    final androidArgs = args['android'] as Map<String, dynamic>? ?? {};
    final iosArgs     = args['ios']     as Map<String, dynamic>? ?? {};
    final autoStart   = args['autoStart'] as bool? ?? false;

    // ── Android foreground notification channel ─────────────────────────
    if (defaultTargetPlatform == TargetPlatform.android) {
      final channelId   = androidArgs['notificationChannelId']   as String? ?? 'flet_bg_service';
      final channelName = androidArgs['notificationChannelName'] as String? ?? 'Background Service';

      final channel = AndroidNotificationChannel(
        channelId,
        channelName,
        importance: Importance.low,  // silent — no sound for the service notification
      );

      await FlutterLocalNotificationsPlugin()
          .resolvePlatformSpecificImplementation<
              AndroidFlutterLocalNotificationsPlugin>()
          ?.createNotificationChannel(channel);
    }

    // ── flutter_background_service configure ────────────────────────────
    await _svc.configure(
      androidConfiguration: AndroidConfiguration(
        onStart:              _onAndroidBackground,
        autoStart:            autoStart,
        isForegroundMode:     androidArgs['isForegroundMode']  as bool? ?? true,
        autoStartOnBoot:      androidArgs['autoStartOnBoot']   as bool? ?? false,
        notificationChannelId:
            androidArgs['notificationChannelId'] as String? ?? 'flet_bg_service',
        initialNotificationTitle:
            androidArgs['initialNotificationTitle'] as String? ?? 'Running in background',
        initialNotificationContent:
            androidArgs['initialNotificationContent'] as String? ?? 'Tap to open',
        foregroundServiceNotificationId:
            androidArgs['notificationId'] as int? ?? 888,
        // Android 14+ foreground service type — must match AndroidManifest.xml
        foregroundServiceTypes: _parseFgServiceType(
          androidArgs['foregroundServiceType'] as String?,
        ),
      ),
      iosConfiguration: IosConfiguration(
        autoStart:    autoStart || (iosArgs['autoStart'] as bool? ?? false),
        onForeground: _onAndroidBackground,  // shared entry point
        onBackground: _onIosBackground,
      ),
    );

    _initialized = true;
  }

  // ── Custom event ──────────────────────────────────────────────────────────

  void _sendCustomEvent(Map<String, dynamic> args) {
    final eventName = args['eventName'] as String? ?? 'custom';
    final data      = args['data']      as Map<String, dynamic>? ?? {};
    _svc.invoke(eventName, data);
  }

  // ── Helpers ───────────────────────────────────────────────────────────────

  List<AndroidForegroundType> _parseFgServiceType(String? raw) {
    switch (raw) {
      case 'location':
        return [AndroidForegroundType.location];
      case 'mediaPlayback':
        return [AndroidForegroundType.mediaPlayback];
      case 'dataSync':
        return [AndroidForegroundType.dataSync];
      case 'health':
        return [AndroidForegroundType.health];
      case 'remoteMessaging':
        return [AndroidForegroundType.remoteMessaging];
      default:
        // connectedDevice covers sensor / accelerometer use cases (SlapPhone)
        return [AndroidForegroundType.connectedDevice];
    }
  }
}