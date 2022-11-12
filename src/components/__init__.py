from typing import Any
from browser import timer
from pyfyre import Style
from pyfyre.nodes import *
from globals.styles import center_xy
from globals.states import nav_is_opened, surprise_message_states
from components.clickables import RouterButton


class Background(Widget):
    def __init__(self) -> None:
        super().__init__(
            styles=[
                Style(
                    width="100vw",
                    height="100vh",
                    position="fixed",
                    z_index="-1000",
                    background_image="url(/images/background.jpg)",
                    background_size="cover",
                    background_position="center",
                    opacity="0.5",
                )
            ],
        )

    def build(self) -> list[Node]:
        return [
            Link(
                "https://twitter.com/adityar51253736/status/1584827745112317953"
                "?t=0518MJBJHHmQZxub23fPhA&s=19",
                lambda: [Text("Background Source")],
                styles=[
                    Style(
                        position="absolute",
                        bottom="0",
                        font_family="Syne Mono",
                        z_index="10000",
                    )
                ],
                attrs={"target": "_blank"},
            )
        ]


class Nav(Widget):
    def __init__(self) -> None:
        super().__init__(
            styles=[
                Style(
                    width="100%",
                    position="fixed",
                    z_index="1000",
                    top="0",
                    background_color="#0009",
                    transition="ease 0.5s",
                    padding_left="20px",
                )
            ],
            states=[nav_is_opened],
        )

    def build(self) -> list[Node]:
        if nav_is_opened.value:
            self.style.update(right="0")
        else:
            self.style.update(right="-100%")

        return [
            Button(
                lambda ev: nav_is_opened.set_value(not nav_is_opened.value),
                styles=[
                    Style(
                        position="fixed",
                        border_radius="100%",
                        width="50px",
                        height="50px",
                        top="7.5px",
                        right="7.5px",
                        background_image="url(/images/avatar.png)",
                        background_size="cover",
                    ),
                ],
            ),
            RouterButton("Home", "/"),
            RouterButton("About", "/about"),
            RouterButton("Skills", "/skills"),
            RouterButton("Projects", "/projects"),
        ]


class SurpriseMessage(Widget):
    def __init__(self) -> None:
        super().__init__(
            styles=[
                center_xy,
                Style(
                    position="fixed",
                    font_size="20vw",
                    z_index="200000",
                ),
            ],
            states=[surprise_message_states["is_active"]],
        )

    def build(self) -> list[Node]:
        if surprise_message_states["is_active"].value:
            self.style.update(
                transition="none",
                visibility="visible",
                opacity="1",
                transform="translate3d(-50%, -50%, 0) scale(2) rotate(-10deg)",
            )
        else:
            self.style.update(
                transition="linear 500ms",
                visibility="hidden",
                opacity="0",
                transform="translate3d(-50%, -50%, 0) scale(0) rotate(-10deg)",
            )

        return [Text(surprise_message_states["text"])]

    @staticmethod
    def show(message: Any) -> None:
        surprise_message_states["text"] = message

        if surprise_message_states["is_active"].value:
            timer.clear_timeout(surprise_message_states["timeout"])
        else:
            surprise_message_states["is_active"].set_value(True)

        surprise_message_states["timeout"] = timer.set_timeout(
            lambda: surprise_message_states["is_active"].set_value(False), 100
        )
