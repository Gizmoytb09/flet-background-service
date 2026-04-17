from __future__ import annotations

from dataclasses import dataclass, field
from enum import StrEnum


class ServiceStatus(StrEnum):
    """Lifecycle states reported by the background service isolate."""

    STARTED   = "service_started"
    STOPPED   = "service_stopped"
    PONG      = "pong"
    UNKNOWN   = "unknown"


class ForegroundServiceType(StrEnum):
    """
    Android 14+ foreground service type declaration.

    Must match the ``foregroundServiceType`` declared in AndroidManifest.xml.
    Choose the narrowest type that fits your use-case to pass Play Store review.

    See: https://developer.android.com/about/versions/14/changes/fgs-types-required
    """

    CONNECTED_DEVICE = "connectedDevice"   # sensor / Bluetooth reading
    DATA_SYNC        = "dataSync"           # uploading / syncing data
    HEALTH           = "health"             # fitness / health tracking
    LOCATION         = "location"           # GPS tracking
    MEDIA_PLAYBACK   = "mediaPlayback"      # audio / video playback
    REMOTE_MESSAGING = "remoteMessaging"    # messaging / VOIP
    SPECIAL_USE      = "specialUse"         # catch-all (requires Play approval)
    SYSTEM_EXEMPTED  = "systemExempted"     # exempt from restrictions


@dataclass(frozen=True, slots=True)
class ServiceEvent:
    """
    Strongly-typed wrapper around event payloads from the Dart isolate.

    Parameters
    ----------
    type:
        Lifecycle or custom event type.
    payload:
        Arbitrary extra data attached by the background isolate.
    """

    type:    ServiceStatus
    payload: dict = field(default_factory=dict)

    @classmethod
    def from_raw(cls, data: dict) -> "ServiceEvent":
        raw_type = data.get("type", "unknown")
        try:
            status = ServiceStatus(raw_type)
        except ValueError:
            status = ServiceStatus.UNKNOWN
        return cls(
            type=status,
            payload={k: v for k, v in data.items() if k != "type"},
        )


@dataclass(slots=True)
class AndroidConfig:
    """
    Android-specific configuration for the background service.

    Parameters
    ----------
    is_foreground_mode:
        Run as an Android foreground service (visible notification, harder
        to kill). Required on Android 8.0+ for long-running work.
    auto_start_on_boot:
        Restart the service automatically after the device reboots.
        Requires ``RECEIVE_BOOT_COMPLETED`` permission in AndroidManifest.xml.
    foreground_service_type:
        Android 14+ foreground service type. Must match the type declared in
        AndroidManifest.xml. Ignored on older API levels.
    notification_channel_id:
        ID of the Android notification channel for the foreground notification.
    notification_channel_name:
        User-visible channel name shown in system notification settings.
    notification_id:
        Android notification ID for the persistent foreground notification.
    initial_notification_title:
        Title shown in the foreground notification while the service runs.
    initial_notification_content:
        Body text shown in the foreground notification.
    """

    is_foreground_mode:           bool               = True
    auto_start_on_boot:           bool               = False
    foreground_service_type:      ForegroundServiceType = ForegroundServiceType.CONNECTED_DEVICE
    notification_channel_id:      str                = "flet_bg_service"
    notification_channel_name:    str                = "Background Service"
    notification_id:              int                = 888
    initial_notification_title:   str                = "Running in background"
    initial_notification_content: str                = "Tap to open"

    def to_dict(self) -> dict:
        return {
            "isForegroundMode":          self.is_foreground_mode,
            "autoStartOnBoot":           self.auto_start_on_boot,
            "foregroundServiceType":     str(self.foreground_service_type),
            "notificationChannelId":     self.notification_channel_id,
            "notificationChannelName":   self.notification_channel_name,
            "notificationId":            self.notification_id,
            "initialNotificationTitle":  self.initial_notification_title,
            "initialNotificationContent":self.initial_notification_content,
        }


@dataclass(slots=True)
class IOSConfig:
    """
    iOS-specific configuration for the background service.

    .. note::
       Apple restricts continuous background execution heavily.
       The service will only run while the app is in the foreground on iOS
       unless you enable the ``background_fetch`` capability in Xcode and
       add the BGTaskScheduler Info.plist keys.

    Parameters
    ----------
    auto_start:
        Start the service when the control mounts (iOS foreground handler).
    """

    auto_start: bool = False

    def to_dict(self) -> dict:
        return {"autoStart": self.auto_start}