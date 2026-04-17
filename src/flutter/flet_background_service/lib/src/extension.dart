// src/flutter/flet_background_service/lib/src/extension.dart
//
// Registers flet_background_service with Flet's FletExtension API.
// Flet calls createService() when it finds a control whose type matches
// the registered string.

import 'package:flet/flet.dart';

import 'background_service_impl.dart';

class Extension extends FletExtension {
  @override
  FletService? createService(Control control) {
    if (control.type == 'flet_background_service') {
      return BackgroundServiceImpl(control: control);
    }
    return null;
  }
}