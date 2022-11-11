from pyfyre import Style
from pyfyre.nodes import *
from styles import mq_mobile, centerx, debug


class Section(Widget):
    def __init__(self, view: Node, *, tag_name: str = "section") -> None:
        self.view = view
        super().__init__(
            tag_name=tag_name,
            styles=[
                centerx,
                debug,
                Style(
                    width="calc(100vw / 1.3)" if mq_mobile.matches else "200px",
                    margin_bottom="40px",
                ),
            ],
        )

    def build(self) -> list[Node]:
        return [self.view]


class Home(Widget):
    def __init__(self) -> None:
        super().__init__(
            tag_name="main", states=[mq_mobile], styles=[Style(padding_top="50px")]
        )

    def build(self) -> list[Node]:
        return [
            Section(
                Element(
                    "img",
                    attrs={"src": "/images/avatar.png"},
                    styles=[
                        Style(
                            border_radius="100%",
                            height="calc(100vw / 1.3)"
                            if mq_mobile.matches
                            else "200px",
                        )
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
                            styles=[Style(font_wight="bold", font_family="Open Sans")],
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
                            text_align="center",
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
                        Element(
                            "img",
                            attrs={
                                "src": "https://media.tenor.com/GttGPkMEhP0AAAAC/anime-what.gif"
                            },
                        ),
                        Element(
                            "p",
                            lambda: [
                                RouterLink(
                                    "/about",
                                    lambda: [Text("Do you wanna know more about me?")],
                                )
                            ],
                            styles=[
                                Style(
                                    font_family="Schoolbell",
                                    font_size="1.7rem",
                                    text_align="center",
                                    line_height="2rem",
                                    margin="20px auto",
                                )
                            ],
                        ),
                    ],
                )
            ),
        ]
