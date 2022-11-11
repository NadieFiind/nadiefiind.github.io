from pyfyre import Style, State
from pyfyre.nodes import *
from styles import mq_mobile, head_style
from widgets import (
    Section,
    MainSection,
    SocMedLink,
    glowing_circle_image,
    image,
    user_action,
)


class Home(MainSection):  # type: ignore[misc]
    def build(self) -> list[Node]:
        show_about_link = State[bool](False)

        return [
            Section(
                glowing_circle_image(
                    "/images/avatar.png",
                    height="calc(100vw / 1.3)" if mq_mobile.matches else "200px",
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
                    styles=[head_style],
                ),
                Element(
                    "span",
                    lambda: [Text("(⁠~⁠￣⁠~⁠￣⁠)⁠~")],
                    styles=[
                        Style(
                            font_size="1.5rem",
                            font_family="monospace",
                            position="relative",
                            top="7px",
                        )
                    ],
                ),
                tag_name="header",
                styles=[Style(white_space="nowrap", line_height="2.5rem")],
            ),
            Section(
                SocMedLink("Discord", "https://discord.com/users/459745032811839500"),
                SocMedLink("GitHub", "https://github.com/NadieFiind"),
                SocMedLink("Twitter", "https://twitter.com/NadieFiind"),
                SocMedLink("Reddit", "https://www.reddit.com/user/NadieFiind"),
                styles=[
                    Style(
                        display="flex",
                        justify_content="space-between",
                        flex_wrap="wrap",
                    )
                ],
            ),
            Section(
                image("https://media.tenor.com/GttGPkMEhP0AAAAC/anime-what.gif"),
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
                            styles=[Style(margin_bottom="10px", display="block")],
                        ),
                        user_action(lambda ev: show_about_link.set_value(True), "Yes!")
                        if not show_about_link.value
                        else user_action("/about", "...", router=True),
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
                states=[show_about_link],
            ),
        ]
