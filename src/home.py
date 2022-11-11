from pyfyre import Style, State
from pyfyre.nodes import *
from widgets import Section, MainSection, SocMedLink
from styles import mq_mobile, head_style, centerx


class Home(MainSection):  # type: ignore[misc]
    def build(self) -> list[Node]:
        show_about_link = State[bool](False)

        return [
            Section(
                Element(
                    "img",
                    attrs={
                        "src": "/images/avatar.png",
                        "class": "glowing-circle" if not mq_mobile.matches else "",
                    },
                    styles=[
                        Style(
                            border_radius="100%",
                            height="calc(100vw / 1.3)"
                            if mq_mobile.matches
                            else "200px",
                        ),
                    ],
                )
            ),
            Section(
                Element(
                    "div",
                    lambda: [
                        Element(
                            "span",
                            lambda: [Text("Hello! It's")],
                            styles=[Style(font_size="1.5rem", font_family="Syne Mono")],
                        ),
                        Element(
                            "h1",
                            lambda: [Text("Nadie Fiind")],
                            styles=[head_style],
                        ),
                        Element(
                            "span",
                            lambda: [Text("(⁠~⁠￣⁠~⁠￣⁠)⁠~")],
                            styles=[Style(font_size="1.5rem", font_family="monospace")],
                        ),
                    ],
                    styles=[
                        Style(
                            font_size="3rem",
                            white_space="nowrap",
                            line_height="2.5rem",
                        )
                    ],
                ),
                tag_name="header",
            ),
            Section(
                Element(
                    "div",
                    lambda: [
                        SocMedLink(
                            "Discord", "https://discord.com/users/459745032811839500"
                        ),
                        SocMedLink("GitHub", "https://github.com/NadieFiind"),
                        SocMedLink("Twitter", "https://twitter.com/NadieFiind"),
                        SocMedLink("Reddit", "https://www.reddit.com/user/NadieFiind"),
                    ],
                    styles=[
                        Style(
                            display="flex",
                            justify_content="space-between",
                            flex_wrap="wrap",
                        )
                    ],
                )
            ),
            Section(
                Element(
                    "div",
                    lambda: [
                        Element(
                            "img",
                            attrs={
                                "src": "https://media.tenor.com/GttGPkMEhP0AAAAC/anime-what.gif"
                            },
                            styles=[centerx],
                        ),
                        Element(
                            "p",
                            lambda: [
                                Element(
                                    "span",
                                    lambda: [
                                        Text(
                                            "Do you wanna know more about me?"
                                            if not show_about_link.value
                                            else "That's kinda weird but ok."
                                        )
                                    ],
                                    styles=[
                                        Style(margin_bottom="10px", display="block")
                                    ],
                                ),
                                Button(
                                    lambda ev: show_about_link.set_value(True),
                                    lambda: [Text("Yes!")],
                                    styles=[
                                        Style(
                                            font_size="1.3rem",
                                            font_family="Syne Mono",
                                        )
                                    ],
                                    attrs={
                                        "class": "glowing"
                                        if not mq_mobile.matches
                                        else ""
                                    },
                                )
                                if not show_about_link.value
                                else RouterLink(
                                    "/about",
                                    lambda: [Text("...")],
                                    styles=[
                                        Style(
                                            font_size="1.3rem",
                                            font_family="Syne Mono",
                                        )
                                    ],
                                    attrs={
                                        "class": "glowing"
                                        if not mq_mobile.matches
                                        else ""
                                    },
                                ),
                            ],
                            styles=[
                                Style(
                                    font_family="Schoolbell",
                                    font_size="1.7rem",
                                    line_height="2rem",
                                    margin="20px auto",
                                )
                            ],
                        ),
                    ],
                    states=[show_about_link],
                )
            ),
        ]
