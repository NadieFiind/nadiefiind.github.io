from pyfyre import Style, State
from pyfyre.nodes import *
from globals.styles import title_style, center_x
from components.sections import MainSection, Section
from components.clickables import AccountLink, RouterButton, ActionButton, external_link
from components.contents import image, dialog_text


class Home(MainSection):
    def build(self) -> list[Node]:
        show_about_link = State[bool](False)

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
                image("https://media.tenor.com/GttGPkMEhP0AAAAC/anime-what.gif"),
                Element(
                    "div",
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
                        ActionButton(lambda ev: show_about_link.set_value(True), "Yes!")
                        if not show_about_link.value
                        else RouterButton("...", "/about"),
                    ],
                    styles=[
                        Style(
                            font_family="Schoolbell",
                            font_size="1.7rem",
                            line_height="2rem",
                            margin="20px auto",
                        )
                    ],
                    states=[show_about_link],
                ),
            ),
            Section(
                image("https://media.tenor.com/7X32PSw9c_EAAAAM/mona-sin-mora.gif"),
                dialog_text("Why is my wallet empty again??? ヽ(　￣д￣)ノ"),
                dialog_text(
                    "(I can make websites and other stuff)",
                    styles=[Style(font_size="1.1rem", margin_bottom="20px")],
                ),
                external_link(
                    "Hire!!",
                    "https://mail.google.com/mail?view=cm&to=nadiefiind@gmail.com",
                ),
            ),
        ]
