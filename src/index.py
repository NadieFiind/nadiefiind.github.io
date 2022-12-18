from typing import Type, Any, Callable
from pyfyre import render, Style
from pyfyre.nodes import *
from components import Background
from components.sections import MainSection, Section
from components.clickables import AccountLink
from components.contents import image
from styles import title_style, center_x


class Home(MainSection):
    def build(self) -> list[Node]:
        return [
            Section(
                Element(
                    "img",
                    attrs={"src": "/images/avatar.png"},
                    styles=[center_x, Style(border_radius="100%", max_width="300px")],
                )
            ),
            Section(
                Element(
                    "span",
                    lambda: [Text("Hello! It's")],
                    styles=[Style(font_size="1.5rem", font_family="Syne Mono")],
                ),
                Element(
                    "h1",
                    lambda: [Text("Nadie Fiind")],
                    styles=[title_style],
                ),
                Element(
                    "span",
                    lambda: [Text("(⁠~⁠￣⁠~⁠￣⁠)⁠~")],
                    styles=[
                        Style(
                            font_size="1.5rem",
                            font_family="monospace",
                            position="relative",
                            top="9px",
                        )
                    ],
                ),
                tag_name="header",
                styles=[Style(white_space="nowrap", line_height="2.5rem")],
            ),
            Section(
                AccountLink("Email", "mailto:nadiefiind@gmail.com"),
                AccountLink("Discord", "https://discord.com/users/459745032811839500"),
                AccountLink("GitHub", "https://github.com/NadieFiind"),
                AccountLink("Itch-io", "https://nadiefiind.itch.io"),
                AccountLink(
                    "HoYoLAB", "https://www.hoyolab.com/accountCenter?id=114221687"
                ),
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
            ),
        ]


def page_builder(main: Type[Widget]) -> Callable[[Any], Element]:
    def route_builder(arg: Any) -> Element:
        return Element(
            "div",
            lambda: [
                Background(),
                main(),
                Link(
                    "https://twitter.com/adityar51253736/status/1584827745112317953"
                    "?t=0518MJBJHHmQZxub23fPhA&s=19",
                    lambda: [Text("Background Source")],
                    styles=[
                        Style(
                            position="fixed",
                            bottom="0",
                            font_family="Syne Mono",
                            opacity="0.5",
                            font_size="1rem",
                            z_index="2000",
                        )
                    ],
                    attrs={"target": "_blank"},
                ),
            ],
            styles=[Style(padding_bottom="20px")],
        )

    return route_builder


render({"/": page_builder(Home)})
