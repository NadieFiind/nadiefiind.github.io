from typing import Any, Tuple
from browser import timer, DOMEvent
from pyfyre import Style, State
from pyfyre.nodes import *
from settings import ROUTES
from styles import center_xy, glossy
from components.sections import Section
from components.clickables import RouterButton, AccountLink, external_link
from components.contents import text


def crypto_addresses() -> Tuple[Element, Element]:
    s = Style(
        position="fixed",
        max_height="0",
        z_index="10000",
        padding="15px",
        left="15px",
        bottom="120px",
        border_radius="10px",
        background_color="white",
        color="black",
        overflow="hidden",
        transition="ease 0.2s",
        visibility="hidden",
        opacity="0",
    )

    def toggle(event: DOMEvent) -> None:
        if s["max_height"] == "100vh":
            s["max_height"] = "0"
            s["visibility"] = "hidden"
            s["opacity"] = "0"
        else:
            s["max_height"] = "100vh"
            s["visibility"] = "visible"
            s["opacity"] = "1"

    return (
        Element(
            "div",
            lambda: [
                Element(
                    "p",
                    lambda: [Text("Support me using cryptocurrency")],
                    styles=[
                        Style(
                            font_family="Poppins",
                            font_weight="bold",
                            text_align="center",
                            margin_bottom="10px",
                        )
                    ],
                ),
                Element(
                    "div",
                    lambda: [
                        text("USDT (SOL) ", styles=[Style(font_weight="bold")]),
                        Element(
                            "code",
                            lambda: [
                                Text("51FHuj1NEKH2EyYNZmFbvdETRe27smyczp4fHQ13RAHJ")
                            ],
                        ),
                    ],
                    styles=[Style(font_size="0.9rem")],
                ),
                Element(
                    "div",
                    lambda: [
                        text("BTC ", styles=[Style(font_weight="bold")]),
                        Element(
                            "code",
                            lambda: [
                                Text("bc1qyr3m2nx80pkt3fu6a2xevx6kaczpfmwkypztdq")
                            ],
                        ),
                    ],
                    styles=[Style(font_size="0.9rem")],
                ),
                Element(
                    "div",
                    lambda: [
                        text("ETH ", styles=[Style(font_weight="bold")]),
                        Element(
                            "code",
                            lambda: [
                                Text("0x8CE6fcC10a0E84024972D99c5b72d12EF6D682b6")
                            ],
                        ),
                    ],
                    styles=[Style(font_size="0.9rem")],
                ),
            ],
            styles=[glossy, s],
        ),
        Button(
            toggle,
            lambda: [
                Element(
                    "i",
                    attrs={"class": "fa-brands fa-bitcoin"},
                    styles=[Style(font_size="40px")],
                )
            ],
            styles=[
                Style(
                    position="fixed",
                    bottom="70px",
                    left="15px",
                    z_index="10001",
                )
            ],
        ),
    )


def social_links() -> Element:
    return Section(
        AccountLink("Gravatar", "https://en.gravatar.com/kylasimp"),
        AccountLink("Ko-fi", "https://ko-fi.com/nadiefiind"),
        AccountLink("GitHub", "https://github.com/NadieFiind"),
        AccountLink("Itch-io", "https://nadiefiind.itch.io"),
        AccountLink("Steam", "https://steamcommunity.com/id/nadiefiind"),
        AccountLink("Top-gg", "https://top.gg/user/363396908136988672"),
        AccountLink("PyPI", "https://pypi.org/user/NadieFiind/"),
        AccountLink("Twitter", "https://twitter.com/NadieFiind"),
        AccountLink("Reddit", "https://www.reddit.com/user/NadieFiind"),
        AccountLink("HoYoLAB", "https://www.hoyolab.com/accountCenter?id=114221687"),
        AccountLink(
            "Spotify",
            "https://open.spotify.com/user/r8fcyujc1i3b2th7p2nd1ut7x?si=3642ee5174e64cb5",
        ),
        AccountLink("TraderSync", "https://shared.tradersync.com/nadiefiind"),
        Element(
            "div",
            lambda: [
                Element(
                    "div",
                    lambda: [
                        text("Email "),
                        external_link(
                            "nadiefiind@gmail.com", "mailto:nadiefiind@gmail.com"
                        ),
                    ],
                    styles=[Style(margin_left="10px", margin_right="10px")],
                ),
                Element(
                    "div",
                    lambda: [
                        text("Discord "),
                        external_link(
                            "Nadie#5944", "https://discord.com/users/459745032811839500"
                        ),
                    ],
                    styles=[Style(margin_left="10px", margin_right="10px")],
                ),
            ],
            styles=[Style(width="100%", display="flex", justify_content="center")],
        ),
        styles=[
            Style(
                display="flex",
                justify_content="center",
                flex_wrap="wrap",
                max_width="800px",
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
                    top="0",
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
                    font_family="Syne Mono",
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
