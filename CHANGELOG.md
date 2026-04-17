# Changelog

All notable changes to **flet-background-service** will be documented in this file.

This project adheres to [Semantic Versioning](https://semver.org/) and [Conventional Commits](https://www.conventionalcommits.org/).

---

## [Unreleased]

> Changes staged for the next release.

---

## [0.1.0] — 2026-04-17 · _Initial Beta Release_

### Added

- **`BackgroundService`** — Non-visual `ft.Service` control that wraps `flutter_background_service`.
  - `initialize(android, ios, auto_start)` — Configure and initialise the plugin.
  - `start()` — Launch the background service.
  - `stop()` — Stop the service gracefully.
  - `ping()` — Send a liveness ping; isolate responds with `ServiceStatus.PONG`.
  - `send(event_name, data)` — Send a custom named event to the Dart isolate.
  - `update_notification(title, content)` — Update the Android foreground notification text.
- **`AndroidConfig`** dataclass with all Android foreground service options:
  - Foreground mode, boot-restart, typed service (Android 14+), notification channel, notification text.
- **`IOSConfig`** dataclass (`auto_start` flag).
- **`ServiceEvent`** — Strongly-typed wrapper for Dart isolate events.
- **`ServiceStatus`** enum (`STARTED`, `STOPPED`, `PONG`, `UNKNOWN`).
- **`ForegroundServiceType`** enum — 8 Android 14+ foreground service types.
- `android_manifest_additions.xml` — Required `AndroidManifest.xml` snippets with inline guidance.
- `ios_info_plist_additions.xml` — Required `Info.plist` keys with inline guidance.
- **SlapPhone demo** (`examples/flet_background_service_example/`) — Full example using accelerometer + foreground notification updates.
- `pyproject.toml` with Hatchling build, Ruff lint rules, and Mypy strict config.

---

[Unreleased]: https://github.com/Gizmoytb09/flet-background-service/compare/v0.1.0...HEAD
[0.1.0]: https://github.com/Gizmoytb09/flet-background-service/releases/tag/v0.1.0
