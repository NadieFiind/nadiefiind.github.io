from pyfyre import Style
from pyfyre.nodes import *
from components.sections import MainSection, Section
from components.clickables import AccountLink, external_link, internal_link
from components.contents import dialog_text, small_text
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
            Section(
                dialog_text(
                    Element(
                        "span",
                        lambda: [
                            Text("I make "),
                            external_link("games", "https://nadiefiind.itch.io"),
                            Text(" and "),
                            external_link("stuff", "https://github.com/NadieFiind"),
                            Text("."),
                        ],
                    )
                ),
                small_text(
                    Element(
                        "span",
                        lambda: [
                            Text("Do you want to commission me? Here are my "),
                            internal_link("services", "/services"),
                            Text("."),
                        ],
                    ),
                    styles=[Style(margin_top="-20px")],
                ),
            ),
        ]
