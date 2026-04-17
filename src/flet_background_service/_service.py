from __future__ import annotations

import json
from collections.abc import Callable

import flet as ft

from ._types import AndroidConfig, IOSConfig, ServiceEvent


@ft.control("flet_background_service")
class BackgroundService(ft.Service):
    """
    Non-visual Flet Service that manages a persistent background service
    powered by ``flutter_background_service`` under the hood.

    Add one instance to your page, call :meth:`initialize` once, then call
    :meth:`start` to launch the service.

    Parameters
    ----------
    on_event:
        Fired when the background isolate emits any event (lifecycle or custom).
        Receives a :class:`~._types.ServiceEvent` instance.

    Examples
    --------
    ::

        import flet as ft
        from flet_background_service import (
            BackgroundService, AndroidConfig, IOSConfig, ServiceEvent, ServiceStatus,
        )

        def main(page: ft.Page) -> None:
            def on_event(event: ServiceEvent) -> None:
                if event.type == ServiceStatus.STARTED:
                    print("Service is live!")

            svc = BackgroundService(on_event=on_event)
            page.add(svc)

            svc.initialize(
                android=AndroidConfig(
                    is_foreground_mode=True,
                    initial_notification_title="SlapPhone",
                    initial_notification_content="Listening for taps…",
                ),
                ios=IOSConfig(auto_start=False),
                auto_start=False,
            )
            svc.start()

        ft.app(main)
    """

    # Reset after each dispatch so a later update() doesn't re-fire the command.
    _command: str | None = None
    _payload: str | None = None

    on_event: Callable[[ServiceEvent], None] | None = None


    def _get_control_name(self) -> str:
        return "flet_background_service"


    def _dispatch(self, command: str, **kwargs: object) -> None:
        """Serialise kwargs → JSON, stamp _command, push one update()."""
        self._command = command
        self._payload = json.dumps(kwargs, default=str)
        self.update()
        # Reset so the next unrelated update() doesn't re-fire the command.
        self._command = None
        self._payload = None

    def initialize(
        self,
        *,
        android: AndroidConfig | None = None,
        ios: IOSConfig | None = None,
        auto_start: bool = False,
    ) -> None:
        """
        Configure and initialise the background service plugin.

        Must be called **once** before :meth:`start`. Safe to call inside
        ``page.on_app_lifecycle_state_change`` or at page load time.

        Parameters
        ----------
        android:
            Android-specific configuration. Defaults to safe defaults if
            omitted.
        ios:
            iOS-specific configuration. Defaults to safe defaults if omitted.
        auto_start:
            If ``True`` the service starts immediately after initialisation
            without an explicit :meth:`start` call.
        """
        self._dispatch(
            "initialize",
            android=(android or AndroidConfig()).to_dict(),
            ios=(ios or IOSConfig()).to_dict(),
            autoStart=auto_start,
        )

    def start(self) -> None:
        """
        Start the background service.

        On Android this launches a foreground service with a persistent
        status-bar notification (required since Android 8.0).
        On iOS this activates the foreground handler; full background
        execution is subject to OS restrictions.
        """
        self._dispatch("start")

    def stop(self) -> None:
        """
        Stop the background service gracefully.

        Sends a ``stop`` invoke to the Dart isolate, which calls
        ``service.stopSelf()``.
        """
        self._dispatch("stop")

    def ping(self) -> None:
        """
        Send a liveness ping to the background isolate.

        The isolate responds with a :attr:`~._types.ServiceStatus.PONG` event
        delivered to :attr:`on_event`. Use this to verify the service is still
        alive without polling.
        """
        self._dispatch("ping")

    def send(self, event_name: str, data: dict | None = None) -> None:
        """
        Send a custom named event **to** the background isolate.

        The Dart isolate receives it via ``service.on(event_name).listen(…)``.

        Parameters
        ----------
        event_name:
            Arbitrary string key the isolate is listening for.
        data:
            Optional JSON-serialisable payload.
        """
        self._dispatch("send", eventName=event_name, data=data or {})

    def update_notification(
        self,
        *,
        title: str,
        content: str,
    ) -> None:
        """
        Update the Android foreground notification text while the service runs.

        No-op on iOS.

        Parameters
        ----------
        title:
            New notification title.
        content:
            New notification body text.
        """
        self._dispatch("updateNotification", title=title, content=content)

    def _handle_service_event(self, e: ft.ControlEvent) -> None:
        """Deserialise raw event dict → ServiceEvent → on_event callback."""
        if self.on_event is None:
            return
        raw = e.data if isinstance(e.data, dict) else {}
        self.on_event(ServiceEvent.from_raw(raw))