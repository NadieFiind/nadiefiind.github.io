from pyfyre import Style
from pyfyre.nodes import *
from components import social_links
from components.sections import MainSection, Section
from components.clickables import external_link, internal_link
from components.contents import strong_text, image, text
from styles import title_style, center_x, glossy


class Home(MainSection):
    def build(self) -> list[Node]:
        return [
            Element(
                "div",
                lambda: [
                    Element(
                        "div",
                        lambda: [
                            Section(
                                Element(
                                    "img",
                                    attrs={"src": "/images/avatar.png"},
                                    styles=[
                                        center_x,
                                        Style(border_radius="100%", max_width="300px"),
                                    ],
                                )
                            ),
                            Section(
                                Element(
                                    "span",
                                    lambda: [Text("Hello! It's")],
                                    styles=[
                                        Style(
                                            font_size="1.5rem", font_family="Syne Mono"
                                        )
                                    ],
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
                                styles=[
                                    Style(
                                        white_space="nowrap",
                                        line_height="2.5rem",
                                        margin_top="30px",
                                        margin_bottom="30px",
                                    )
                                ],
                            ),
                            social_links(),
                        ],
                        styles=[center_x],
                    )
                ],
                styles=[
                    Style(min_height="636px", padding_top="40px", padding_bottom="40px")
                ],
            ),
            Element(
                "div",
                lambda: [
                    Element(
                        "div",
                        lambda: [
                            image(
                                "https://media.tenor.com/o-wNCEq_6f0AAAAd/pompo-the-cinephile-typing-fast.gif",
                                width="300px",
                            ),
                            Element(
                                "div",
                                lambda: [
                                    strong_text(
                                        Element(
                                            "span",
                                            lambda: [
                                                Text("I make "),
                                                external_link(
                                                    "games",
                                                    "https://nadiefiind.itch.io",
                                                ),
                                                Text(" and "),
                                                external_link(
                                                    "stuff",
                                                    "https://github.com/NadieFiind",
                                                ),
                                                Text("."),
                                            ],
                                        ),
                                    ),
                                    text(" Try them out (人ゝω・）"),
                                    Element("br"),
                                    Element("br"),
                                    text(
                                        "I am a self-taught programmer and an indie game developer."
                                    ),
                                ],
                                styles=[Style(padding="20px 40px 0 40px")],
                            ),
                        ],
                        styles=[
                            Style(
                                display="flex",
                                justify_content="center",
                                flex_wrap="wrap",
                            )
                        ],
                    ),
                ],
                styles=[glossy, Style(padding_top="50px", padding_bottom="50px")],
            ),
        ]
