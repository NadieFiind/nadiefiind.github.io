from typing import Any
from browser import timer
from pyfyre import Style, State
from pyfyre.nodes import *
from settings import ROUTES
from styles import center_xy
from components.sections import Section
from components.clickables import RouterButton, AccountLink


def social_links() -> Element:
    return Section(
        AccountLink("Email", "mailto:nadiefiind@gmail.com"),
        AccountLink("Discord", "https://discord.com/users/459745032811839500"),
        AccountLink("GitHub", "https://github.com/NadieFiind"),
        AccountLink("Itch-io", "https://nadiefiind.itch.io"),
        AccountLink("HoYoLAB", "https://www.hoyolab.com/accountCenter?id=114221687"),
        AccountLink("Reddit", "https://www.reddit.com/user/NadieFiind"),
        AccountLink("Twitter", "https://twitter.com/NadieFiind"),
        AccountLink(
            "Spotify",
            "https://open.spotify.com/user/r8fcyujc1i3b2th7p2nd1ut7x?si=3642ee5174e64cb5",
        ),
        AccountLink("Steam", "https://steamcommunity.com/id/nadiefiind"),
        AccountLink("YouTube", "https://www.youtube.com/@nadiefiind"),
        AccountLink("Twitch", "https://www.twitch.tv/nadiefiind"),
        styles=[
            Style(
                display="flex",
                justify_content="space-around",
                flex_wrap="wrap",
            )
        ],
    )


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
        return []


class Nav(Widget):
    def __init__(self) -> None:
        self.is_opened = State[bool](False)
        super().__init__(
            styles=[
                Style(
                    width="100%",
                    position="fixed",
                    z_index="1000",
                    top="0",
                    background_color="#0009",
                    transition="ease 0.5s",
                    padding_right="50px",
                    text_align="right",
                )
            ],
            states=[self.is_opened],
        )

    def build(self) -> list[Node]:
        if self.is_opened.value:
            self.style.update(left="0")
        else:
            self.style.update(left="-100%")

        return [
            Button(
                lambda ev: self.is_opened.set_value(not self.is_opened.value),
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
            *(
                RouterButton(route[1:].capitalize() or "Home", route)
                for route in ROUTES
            ),
        ]


class SurpriseMessage(Widget):
    def __init__(self) -> None:
        self.is_active = State[bool](False)
        self.timeout = None
        self.text = ""

        super().__init__(
            styles=[
                center_xy,
                Style(
                    top="40%",
                    position="fixed",
                    font_size="20vw",
                    z_index="200000",
                    font_family="Schoolbell",
                ),
            ],
            states=[self.is_active],
        )

    def build(self) -> list[Node]:
        if self.is_active.value:
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

        return [Text(self.text)]

    def show(self, message: Any) -> None:
        self.text = message

        if self.is_active.value:
            timer.clear_timeout(self.timeout)
        else:
            self.is_active.set_value(True)

        self.timeout = timer.set_timeout(lambda: self.is_active.set_value(False), 100)
