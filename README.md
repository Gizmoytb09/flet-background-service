<div align="center">

<!-- ═══════════════════════  HERO BANNER  ═══════════════════════ -->
<picture>
  <source media="(prefers-color-scheme: dark)" srcset="https://capsule-render.vercel.app/api?type=waving&color=gradient&customColorList=12,20,24&height=220&section=header&text=flet-background-service&fontSize=42&fontColor=ffffff&fontAlignY=38&desc=Persistent%20background%20execution%20for%20Flet%20apps%20%E2%80%94%20Android%20%26%20iOS&descAlignY=62&descSize=16&animation=fadeIn"/>
  <img src="https://capsule-render.vercel.app/api?type=waving&color=gradient&customColorList=12,20,24&height=220&section=header&text=flet-background-service&fontSize=42&fontColor=ffffff&fontAlignY=38&desc=Persistent%20background%20execution%20for%20Flet%20apps%20%E2%80%94%20Android%20%26%20iOS&descAlignY=62&descSize=16&animation=fadeIn" alt="flet-background-service banner"/>
</picture>

<!-- ═══════════════════════  BADGES ROW  ═══════════════════════ -->

<p>
  <a href="https://pypi.org/project/flet-background-service/">
    <img src="https://img.shields.io/pypi/v/flet-background-service?style=for-the-badge&logo=pypi&logoColor=white&color=0d6efd" alt="PyPI version"/>
  </a>
  &nbsp;
  <a href="https://pypi.org/project/flet-background-service/">
    <img src="https://img.shields.io/pypi/dm/flet-background-service?style=for-the-badge&logo=pypi&logoColor=white&color=6366f1" alt="PyPI downloads"/>
  </a>
  &nbsp;
  <a href="#">
    <img src="https://img.shields.io/badge/status-Beta-orange?style=for-the-badge&logo=statuspage&logoColor=white" alt="Beta status"/>
  </a>
  &nbsp;
  <a href="https://www.python.org/downloads/">
    <img src="https://img.shields.io/badge/python-3.12%2B-blue?style=for-the-badge&logo=python&logoColor=white" alt="Python 3.12+"/>
  </a>
  &nbsp;
  <a href="https://flet.dev">
    <img src="https://img.shields.io/badge/flet-%3E%3D0.83.0-7c3aed?style=for-the-badge&logo=flutter&logoColor=white" alt="Flet ≥0.83.0"/>
  </a>
  &nbsp;
  <a href="LICENSE">
    <img src="https://img.shields.io/badge/license-MIT-22c55e?style=for-the-badge&logo=opensourceinitiative&logoColor=white" alt="MIT License"/>
  </a>
</p>

<p>
  <a href="https://github.com/Gizmoytb09/flet-background-service/actions/workflows/ci.yml">
    <img src="https://img.shields.io/github/actions/workflow/status/Gizmoytb09/flet-background-service/ci.yml?branch=main&style=flat-square&label=CI&logo=githubactions&logoColor=white" alt="CI status"/>
  </a>
  &nbsp;
  <a href="https://github.com/Gizmoytb09/flet-background-service/actions/workflows/publish.yml">
    <img src="https://img.shields.io/github/actions/workflow/status/Gizmoytb09/flet-background-service/publish.yml?style=flat-square&label=PyPI%20Publish&logo=githubactions&logoColor=white&color=0d6efd" alt="Publish status"/>
  </a>
  &nbsp;
  <a href="https://github.com/Gizmoytb09/flet-background-service/issues">
    <img src="https://img.shields.io/github/issues/Gizmoytb09/flet-background-service?style=flat-square&color=f59e0b" alt="Open Issues"/>
  </a>
  &nbsp;
  <a href="https://github.com/Gizmoytb09/flet-background-service/pulls">
    <img src="https://img.shields.io/github/issues-pr/Gizmoytb09/flet-background-service?style=flat-square&color=6366f1" alt="Pull Requests"/>
  </a>
  &nbsp;
  <img src="https://img.shields.io/badge/platform-Android%20%7C%20iOS-success?style=flat-square&logo=android" alt="Platform"/>
</p>


---

<!-- ═══════════════════════  BETA NOTICE  ═══════════════════════ -->

<table>
<tr>
<td>

```
⚠️  BETA DEVELOPMENT — v0.1.0
```

> **This library is in active Beta development.**  
> APIs may change between minor versions without prior notice.  
> We welcome issues, feedback, and pull requests — see [CONTRIBUTING.md](CONTRIBUTING.md).

</td>
</tr>
</table>

</div>

---

## 📖 Table of Contents

<div align="center">

| Section | Description |
|---------|-------------|
| [✨ Features](#-features) | What this library does |
| [⚙️ Installation](#%EF%B8%8F-installation) | How to install |
| [🚀 Quick Start](#-quick-start) | Up and running in minutes |
| [🗂️ Project Structure](#%EF%B8%8F-project-structure) | Source layout |
| [📚 API Reference](#-api-reference) | Full class & method documentation |
| [🤖 Android Setup](#-android-setup) | Manifest additions & permissions |
| [🍎 iOS Setup](#-ios-setup) | Info.plist keys & limitations |
| [💡 Examples](#-examples) | Real-world usage |
| [🔄 Changelog](#-changelog) | Release history |
| [🤝 Contributing](#-contributing) | How to contribute |
| [📄 License](#-license) | MIT License |

</div>

---

## ✨ Features

<div align="center">

<table>
<tr>
<td align="center" width="33%">

### 🤖 Android
Foreground Service with persistent status-bar notification.<br/>
Boot-on-restart support.<br/>
Android 14+ typed foreground service.

</td>
<td align="center" width="33%">

### 🍎 iOS
Background fetch + BGTaskScheduler<br/>
integration via `flutter_background_service`.<br/>
Info.plist snippet included.

</td>
<td align="center" width="33%">

### 🐍 Pure Python
Clean Pythonic API over the<br/>
`flutter_background_service` plugin.<br/>
No Dart knowledge required.

</td>
</tr>
</table>

</div>

- **`BackgroundService`** — Non-visual `ft.Service` control: `initialize()`, `start()`, `stop()`, `ping()`, `send()`, `update_notification()`
- **`AndroidConfig`** — Dataclass covering every Android option (foreground mode, boot restart, typed service, notification text)
- **`IOSConfig`** — Minimal iOS config with `auto_start` flag
- **`ServiceEvent`** — Strongly-typed event wrapper (`ServiceStatus.STARTED | STOPPED | PONG | UNKNOWN`)
- **`ForegroundServiceType`** — Android 14+ foreground service type enum (8 types)
- Zero extra Python dependencies beyond `flet >= 0.83.0`

---

## ⚙️ Installation

```bash
pip install flet-background-service
```

> **Requires Python 3.12+** and **Flet ≥ 0.83.0**.

For development / editable install:

```bash
git clone https://github.com/yourorg/flet-background-service.git
cd flet-background-service
pip install -e ".[dev]"
```

---

## 🚀 Quick Start

```python
import flet as ft
from flet_background_service import (
    AndroidConfig,
    BackgroundService,
    ForegroundServiceType,
    IOSConfig,
    ServiceEvent,
    ServiceStatus,
)


def main(page: ft.Page) -> None:
    page.title = "My App"

    def on_event(event: ServiceEvent) -> None:
        if event.type == ServiceStatus.STARTED:
            print("✅ Background service is live!")
        elif event.type == ServiceStatus.STOPPED:
            print("🔴 Background service stopped.")
        elif event.type == ServiceStatus.PONG:
            print("💓 Service is still alive.")

    svc = BackgroundService(on_event=on_event)
    page.add(svc)

    svc.initialize(
        android=AndroidConfig(
            is_foreground_mode=True,
            initial_notification_title="My App",
            initial_notification_content="Running in the background…",
        ),
        ios=IOSConfig(auto_start=False),
        auto_start=False,
    )
    svc.start()


ft.app(main)
```

---

## 🗂️ Project Structure

```
flet-background-service/
├── src/
│   └── flet_background_service/
│       ├── __init__.py          # Public re-exports & __version__
│       ├── _service.py          # BackgroundService (ft.Service subclass)
│       └── _types.py            # AndroidConfig, IOSConfig, ServiceEvent, enums
├── src/
│   └── flutter/                 # Dart plugin side (flutter_background_service wrapper)
├── examples/
│   └── flet_background_service_example/
│       └── main.py              # SlapPhone demo app
├── android_manifest_additions.xml   # Required AndroidManifest.xml snippets
├── ios_info_plist_additions.xml     # Required Info.plist keys
├── pyproject.toml
├── CHANGELOG.md
├── CONTRIBUTING.md
└── LICENSE
```

---

## 📚 API Reference

### `BackgroundService`

```python
@ft.control("flet_background_service")
class BackgroundService(ft.Service):
    ...
```

A non-visual Flet `Service` control. Add **one instance** to your page, call `initialize()` once, then call `start()`.

| Parameter | Type | Description |
|-----------|------|-------------|
| `on_event` | `Callable[[ServiceEvent], None] \| None` | Fired whenever the background isolate emits any event |

#### Methods

---

##### `initialize(*, android, ios, auto_start) → None`

Configure and initialise the background service plugin. **Must be called once** before `start()`.

```python
svc.initialize(
    android=AndroidConfig(
        is_foreground_mode=True,
        auto_start_on_boot=False,
        foreground_service_type=ForegroundServiceType.CONNECTED_DEVICE,
        notification_channel_id="my_channel",
        notification_channel_name="My Background Task",
        notification_id=1001,
        initial_notification_title="My App",
        initial_notification_content="Running…",
    ),
    ios=IOSConfig(auto_start=False),
    auto_start=False,
)
```

| Parameter | Type | Default | Description |
|-----------|------|---------|-------------|
| `android` | `AndroidConfig \| None` | `AndroidConfig()` | Android-specific config |
| `ios` | `IOSConfig \| None` | `IOSConfig()` | iOS-specific config |
| `auto_start` | `bool` | `False` | Start immediately after initialisation |

---

##### `start() → None`

Start the background service.

```python
svc.start()
```

- **Android**: Launches a foreground service with a persistent status-bar notification (required since Android 8.0 / Oreo).
- **iOS**: Activates the foreground handler; full background execution is subject to OS restrictions.

---

##### `stop() → None`

Stop the background service gracefully.

```python
svc.stop()
```

Sends a `stop` invoke to the Dart isolate, which calls `service.stopSelf()`.

---

##### `ping() → None`

Send a liveness ping to the background isolate.

```python
svc.ping()
# The isolate responds with ServiceStatus.PONG → on_event callback
```

The isolate responds with a `ServiceStatus.PONG` event. Use this to verify the service is alive without polling.

---

##### `send(event_name, data) → None`

Send a custom named event **to** the background isolate.

```python
svc.send("my_event", {"key": "value"})
```

| Parameter | Type | Default | Description |
|-----------|------|---------|-------------|
| `event_name` | `str` | required | Arbitrary string key the isolate listens for |
| `data` | `dict \| None` | `{}` | Optional JSON-serialisable payload |

---

##### `update_notification(*, title, content) → None`

Update the Android foreground notification text while the service is running. **No-op on iOS.**

```python
svc.update_notification(
    title="My App — 42 events",
    content="Last event: 3 seconds ago",
)
```

| Parameter | Type | Description |
|-----------|------|-------------|
| `title` | `str` | New notification title |
| `content` | `str` | New notification body text |

---

### `AndroidConfig`

```python
@dataclass(slots=True)
class AndroidConfig:
    is_foreground_mode: bool = True
    auto_start_on_boot: bool = False
    foreground_service_type: ForegroundServiceType = ForegroundServiceType.CONNECTED_DEVICE
    notification_channel_id: str = "flet_bg_service"
    notification_channel_name: str = "Background Service"
    notification_id: int = 888
    initial_notification_title: str = "Running in background"
    initial_notification_content: str = "Tap to open"
```

| Field | Type | Default | Description |
|-------|------|---------|-------------|
| `is_foreground_mode` | `bool` | `True` | Run as an Android foreground service (required on Android 8.0+) |
| `auto_start_on_boot` | `bool` | `False` | Restart the service after device reboot. Requires `RECEIVE_BOOT_COMPLETED` permission |
| `foreground_service_type` | `ForegroundServiceType` | `CONNECTED_DEVICE` | Android 14+ foreground service type. Must match `AndroidManifest.xml` |
| `notification_channel_id` | `str` | `"flet_bg_service"` | Android notification channel ID |
| `notification_channel_name` | `str` | `"Background Service"` | User-visible channel name in system settings |
| `notification_id` | `int` | `888` | Android notification ID for the persistent notification |
| `initial_notification_title` | `str` | `"Running in background"` | Notification title |
| `initial_notification_content` | `str` | `"Tap to open"` | Notification body text |

---

### `IOSConfig`

```python
@dataclass(slots=True)
class IOSConfig:
    auto_start: bool = False
```

| Field | Type | Default | Description |
|-------|------|---------|-------------|
| `auto_start` | `bool` | `False` | Start the service when the control mounts (iOS foreground handler) |

> **Note:** Apple restricts continuous background execution heavily. The service will only run while the app is in the foreground on iOS unless you enable `background_fetch` capability in Xcode and add `BGTaskScheduler` Info.plist keys.

---

### `ServiceEvent`

```python
@dataclass(frozen=True, slots=True)
class ServiceEvent:
    type: ServiceStatus
    payload: dict = field(default_factory=dict)
```

A strongly-typed wrapper around event payloads from the Dart isolate.

| Field | Type | Description |
|-------|------|-------------|
| `type` | `ServiceStatus` | Lifecycle or custom event type |
| `payload` | `dict` | Arbitrary extra data attached by the background isolate |

#### `ServiceEvent.from_raw(data: dict) → ServiceEvent`

Construct a `ServiceEvent` from a raw Dart event dictionary.

---

### `ServiceStatus`

```python
class ServiceStatus(StrEnum):
    STARTED = "service_started"
    STOPPED = "service_stopped"
    PONG    = "pong"
    UNKNOWN = "unknown"
```

| Value | String | Description |
|-------|--------|-------------|
| `STARTED` | `"service_started"` | Service successfully launched |
| `STOPPED` | `"service_stopped"` | Service has stopped |
| `PONG` | `"pong"` | Response to a `ping()` call |
| `UNKNOWN` | `"unknown"` | Custom or unrecognised event |

---

### `ForegroundServiceType`

Android 14+ foreground service type declaration. Must match the `foregroundServiceType` declared in `AndroidManifest.xml`.

```python
class ForegroundServiceType(StrEnum):
    CONNECTED_DEVICE = "connectedDevice"   # sensor / Bluetooth reading
    DATA_SYNC        = "dataSync"          # uploading / syncing data
    HEALTH           = "health"            # fitness / health tracking
    LOCATION         = "location"          # GPS tracking
    MEDIA_PLAYBACK   = "mediaPlayback"     # audio / video playback
    REMOTE_MESSAGING = "remoteMessaging"   # messaging / VOIP
    SPECIAL_USE      = "specialUse"        # catch-all (requires Play approval)
    SYSTEM_EXEMPTED  = "systemExempted"    # exempt from restrictions
```

> Choose the **narrowest type** that fits your use-case to pass Play Store review.  
> See: [Android Docs — FGS Types](https://developer.android.com/about/versions/14/changes/fgs-types-required)

---

## 🤖 Android Setup

Before running on Android, add the following to your `android/app/src/main/AndroidManifest.xml`:

```xml
<!-- ── Permissions (inside <manifest> tag) ─────────────────────────────── -->

<!-- Required: run a foreground service -->
<uses-permission android:name="android.permission.FOREGROUND_SERVICE" />

<!-- Required on Android 14+ for connectedDevice foreground service type -->
<uses-permission android:name="android.permission.FOREGROUND_SERVICE_CONNECTED_DEVICE" />

<!-- Add whichever type matches your AndroidConfig.foreground_service_type: -->
<!-- android.permission.FOREGROUND_SERVICE_LOCATION        → location        -->
<!-- android.permission.FOREGROUND_SERVICE_MEDIA_PLAYBACK  → mediaPlayback   -->
<!-- android.permission.FOREGROUND_SERVICE_DATA_SYNC       → dataSync        -->
<!-- android.permission.FOREGROUND_SERVICE_HEALTH          → health          -->

<!-- Required: restart service after device reboot (if auto_start_on_boot=True) -->
<uses-permission android:name="android.permission.RECEIVE_BOOT_COMPLETED" />

<!-- Required: prevent battery optimisation from killing the service -->
<uses-permission android:name="android.permission.REQUEST_IGNORE_BATTERY_OPTIMIZATIONS" />

<!-- Required on Android 13+ to show the foreground notification -->
<uses-permission android:name="android.permission.POST_NOTIFICATIONS" />


<!-- ── Service declaration (inside <application> tag) ─────────────────── -->

<service
    android:name="id.flutter.flutter_background_service.BackgroundService"
    android:foregroundServiceType="connectedDevice"
    android:exported="false" />
```

> **Change `foregroundServiceType`** to match your use case (`location`, `mediaPlayback`, `dataSync`, `health`, etc.).  
> The value **must match** both `AndroidConfig.foreground_service_type` in Python **and** the `uses-permission` declared above.

---

## 🍎 iOS Setup

Add the following keys to `ios/Runner/Info.plist`:

```xml
<!-- Enable background fetch + processing (required for iOS background execution) -->
<key>UIBackgroundModes</key>
<array>
    <string>fetch</string>
    <string>processing</string>
</array>

<!-- BGTaskScheduler permitted identifiers (iOS 13+) -->
<!-- flutter_background_service uses this task ID internally -->
<key>BGTaskSchedulerPermittedIdentifiers</key>
<array>
    <string>dev.flutter.background_service</string>
</array>
```

> **iOS Limitations:** Even with these keys, Apple restricts when background tasks run. The OS decides the actual frequency — typically every 15–30 minutes at best.  
> The background handler is useful for syncing data, updating notification content, and light processing tasks. It is **not** suitable for continuous sensor reading on iOS.

---

## 💡 Examples

### SlapPhone Demo (`examples/flet_background_service_example/`)

A full example app that uses `BackgroundService` together with the device accelerometer to count "slaps". The foreground notification is updated in real time via `update_notification()`.

```python
from __future__ import annotations

import math

import flet as ft
from flet_background_service import (
    AndroidConfig,
    BackgroundService,
    ForegroundServiceType,
    IOSConfig,
    ServiceEvent,
    ServiceStatus,
)

SLAP_THRESHOLD = 15.0   # m/s² — magnitude that counts as a slap


def main(page: ft.Page) -> None:
    page.title = "flet-background-service demo"
    page.theme_mode = ft.ThemeMode.DARK

    slap_count: list[int] = [0]

    def on_service_event(event: ServiceEvent) -> None:
        match event.type:
            case ServiceStatus.STARTED:
                print("Service started ✅")
            case ServiceStatus.STOPPED:
                print("Service stopped 🔴")
            case ServiceStatus.PONG:
                print("Pong received 💓 — service is alive")
            case ServiceStatus.UNKNOWN:
                raw_type = event.payload.get("type", "")
                if raw_type == "custom":
                    print(f"Custom event: {event.payload}")

    svc = BackgroundService(on_event=on_service_event)
    page.add(svc)

    def on_accelerometer(e: ft.UserAccelerometerEvent) -> None:
        magnitude = math.sqrt(e.x**2 + e.y**2 + e.z**2)
        if magnitude > SLAP_THRESHOLD:
            slap_count[0] += 1
            svc.update_notification(
                title=f"SlapPhone — {slap_count[0]} slaps",
                content=f"Last force: {magnitude:.1f} m/s²",
            )

    accel = ft.UserAccelerometer(
        interval=ft.Duration(milliseconds=50),
        on_reading=on_accelerometer,
    )
    page.add(accel)

    svc.initialize(
        android=AndroidConfig(
            is_foreground_mode=True,
            foreground_service_type=ForegroundServiceType.CONNECTED_DEVICE,
            notification_channel_id="slapphone_bg",
            notification_channel_name="SlapPhone Background",
            notification_id=1001,
            initial_notification_title="SlapPhone",
            initial_notification_content="Listening for taps…",
        ),
        ios=IOSConfig(auto_start=False),
        auto_start=False,
    )
    svc.start()


ft.app(main)
```

### Handling Custom Events from Dart

```python
def on_event(event: ServiceEvent) -> None:
    if event.type == ServiceStatus.UNKNOWN:
        # Custom events from the background Dart isolate land here
        event_name = event.payload.get("type", "")
        if event_name == "location_update":
            lat = event.payload.get("lat")
            lon = event.payload.get("lon")
            print(f"Location: {lat}, {lon}")

svc = BackgroundService(on_event=on_event)
```

### Sending Events To the Dart Isolate

```python
# Send a custom named event to the background Dart isolate
svc.send("pause_tracking", {"reason": "user_request"})

# The Dart isolate listens with:
# service.on('pause_tracking').listen((event) { ... })
```

### Lifecycle-Aware Initialisation

```python
def bootstrap(_=None) -> None:
    svc.initialize(android=AndroidConfig(), ios=IOSConfig(), auto_start=False)

# Re-initialise when the app comes back to the foreground
page.on_app_lifecycle_state_change = lambda e: (
    bootstrap() if e.state == ft.AppLifecycleState.RESUME else None
)
bootstrap()  # Also run on first load
```

---

## 🔄 Changelog

See [CHANGELOG.md](CHANGELOG.md) for the full release history.

---

## 🤝 Contributing

Contributions are welcome! Please read [CONTRIBUTING.md](CONTRIBUTING.md) first.

```
1. Fork the repository
2. Create a feature branch  →  git checkout -b feat/my-feature
3. Make your changes
4. Run linting             →  ruff check src/ && mypy src/
5. Commit your changes     →  git commit -m "feat: my feature"
6. Push to the branch      →  git push origin feat/my-feature
7. Open a Pull Request
```

---

## 📄 License

This project is licensed under the **MIT License** — see the [LICENSE](LICENSE) file for details.

---

<div align="center">

<picture>
  <source media="(prefers-color-scheme: dark)" srcset="https://capsule-render.vercel.app/api?type=waving&color=gradient&customColorList=12,20,24&height=100&section=footer&animation=fadeIn"/>
  <img src="https://capsule-render.vercel.app/api?type=waving&color=gradient&customColorList=12,20,24&height=100&section=footer&animation=fadeIn" alt="footer wave"/>
</picture>

<sub>Built with ❤️ for the <a href="https://flet.dev">Flet</a> community · <a href="https://github.com/Gizmoytb09/flet-background-service/issues">Report a Bug</a> · <a href="https://github.com/Gizmoytb09/flet-background-service/issues">Request a Feature</a></sub>

</div>
