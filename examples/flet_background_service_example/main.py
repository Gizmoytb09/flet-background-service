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
    page.title    = "flet-background-service demo"
    page.theme_mode = ft.ThemeMode.DARK
    page.scroll  = ft.ScrollMode.AUTO

    slap_count: list[int] = [0]   # mutable int inside a list (closure-friendly)

    log_list = ft.ListView(height=220, spacing=2, auto_scroll=True)

    def log(msg: str) -> None:
        log_list.controls.append(
            ft.Text(f"› {msg}", size=11, font_family="monospace")
        )
        page.update()

    status_chip  = ft.Chip(label=ft.Text("Stopped"), bgcolor=ft.Colors.RED_900)
    slap_counter = ft.Text("Slaps: 0", size=28, weight=ft.FontWeight.BOLD)

    def set_status(running: bool) -> None:
        status_chip.label   = ft.Text("Running" if running else "Stopped")
        status_chip.bgcolor = ft.Colors.GREEN_800 if running else ft.Colors.RED_900
        page.update()

    def on_service_event(event: ServiceEvent) -> None:
        match event.type:
            case ServiceStatus.STARTED:
                log("Service started ✅")
                set_status(True)

            case ServiceStatus.STOPPED:
                log("Service stopped 🔴")
                set_status(False)

            case ServiceStatus.PONG:
                log("Pong received 💓 — service is alive")

            case ServiceStatus.UNKNOWN:
                raw_type = event.payload.get("type", "")
                if raw_type == "custom":
                    log(f"Custom event: {event.payload}")
                else:
                    log(f"Unknown event: {event.payload}")

        page.update()

    svc = BackgroundService(on_event=on_service_event)
    page.add(svc)

    def on_accelerometer(e: ft.UserAccelerometerEvent) -> None:
        magnitude = math.sqrt(e.x**2 + e.y**2 + e.z**2)
        if magnitude > SLAP_THRESHOLD:
            slap_count[0] += 1
            slap_counter.value = f"Slaps: {slap_count[0]}"
            svc.update_notification(
                title=f"SlapPhone — {slap_count[0]} slaps",
                content=f"Last force: {magnitude:.1f} m/s²",
            )
            log(f"Slap! magnitude={magnitude:.1f} total={slap_count[0]}")
            page.update()

    accel = ft.UserAccelerometer(
        interval=ft.Duration(milliseconds=50),
        on_reading=on_accelerometer,
    )
    page.add(accel)

    def bootstrap(_: ft.ControlEvent | None = None) -> None:
        svc.initialize(
            android=AndroidConfig(
                is_foreground_mode=True,
                auto_start_on_boot=False,
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
        log("Plugin initialised")

    page.on_app_lifecycle_state_change = lambda e: (
        bootstrap() if e.state == ft.AppLifecycleState.RESUME else None
    )
    bootstrap()

    def btn_start(_: ft.ControlEvent) -> None:
        svc.start()
        log("start() called")

    def btn_stop(_: ft.ControlEvent) -> None:
        svc.stop()
        log("stop() called")

    def btn_ping(_: ft.ControlEvent) -> None:
        svc.ping()
        log("ping() sent")

    def btn_send(_: ft.ControlEvent) -> None:
        svc.send("custom", {"greeting": "hello from Python!"})
        log("custom event sent")

    def btn_update_notif(_: ft.ControlEvent) -> None:
        svc.update_notification(
            title="SlapPhone active",
            content=f"{slap_count[0]} slaps so far",
        )
        log("notification updated")

    page.add(
        ft.Column(
            spacing=16,
            controls=[
                ft.Row(
                    controls=[
                        ft.Text(
                            "flet-background-service",
                            size=22,
                            weight=ft.FontWeight.BOLD,
                        ),
                        status_chip,
                    ],
                    alignment=ft.MainAxisAlignment.SPACE_BETWEEN,
                ),
                slap_counter,
                ft.Divider(),
                ft.Text("Service controls", weight=ft.FontWeight.W_600),
                ft.Wrap(
                    spacing=8,
                    run_spacing=8,
                    controls=[
                        ft.ElevatedButton("Start",               on_click=btn_start),
                        ft.ElevatedButton("Stop",                on_click=btn_stop),
                        ft.OutlinedButton("Ping",                on_click=btn_ping),
                        ft.OutlinedButton("Send custom event",   on_click=btn_send),
                        ft.TextButton("Update notification",     on_click=btn_update_notif),
                    ],
                ),
                ft.Divider(),
                ft.Text("Event log", weight=ft.FontWeight.W_600),
                ft.Container(
                    content=log_list,
                    border=ft.border.all(1, ft.Colors.OUTLINE),
                    border_radius=8,
                    padding=8,
                    expand=True,
                ),
            ],
        )
    )


ft.app(main)