from typing import Any, Callable
from browser import DOMEvent, window
from pyfyre import Style
from pyfyre.nodes import *
from globals.styles import center_y


class ActionButton(Widget):
    def __init__(self, onclick: Callable[[DOMEvent], None], text: Any) -> None:
        self.onclick = onclick
        self.text = text
        super().__init__(styles=[Style(margin="20px auto")])

    def build(self) -> list[Node]:
        return [
            Button(
                self.onclick,
                lambda: [Text(self.text)],
                styles=[
                    Style(
                        font_size="1.3rem",
                        font_family="Syne Mono",
                        text_decoration="underline",
                    )
                ],
            )
        ]


class RouterButton(Widget):
    def __init__(self, text: Any, url: str) -> None:
        self.text = text
        self.url = url
        super().__init__(styles=[Style(margin="20px")])

    def build(self) -> list[Node]:
        router = RouterLink(
            self.url,
            lambda: [Text(self.text)],
            styles=[
                Style(
                    font_size="1.3rem",
                    font_family="Syne Mono",
                    text_decoration="underline",
                )
            ],
            force_build=True,
        )

        def onclick(event: DOMEvent) -> None:
            window.scrollTo({"top": 0, "behavior": "smooth"})

        router.add_event_listener("click", onclick)
        return [router]


class AccountLink(Widget):
    def __init__(self, name: str, url: str, **kwargs: Any) -> None:
        self.name = name
        self.url = url

        style = Style(font_size="2.5rem", margin="0 10px")
        if kwargs.get("styles"):
            kwargs["styles"].append(style)
        else:
            kwargs["styles"] = [style]

        super().__init__(**kwargs)

    def build(self) -> list[Node]:
        def icon() -> Element:
            if self.name.lower() == "email":
                return Element("i", attrs={"class": "fa-solid fa-envelope"})
            elif self.name.lower() == "hoyolab":
                return Element(
                    "img",
                    attrs={
                        "src": "https://cdn.discordapp.com/attachments/10313797"
                        "67674556436/1040654731049181285/hoyolab.png"
                    },
                    styles=[center_y, Style(height="2.5rem")],
                )

            return Element("i", attrs={"class": f"fa-brands fa-{self.name.lower()}"})

        return [Link(self.url, lambda: [icon()], attrs={"target": "_blank"})]


def external_link(text: Any, url: str) -> Element:
    return Element(
        "div",
        lambda: [
            Link(
                url,
                lambda: [Text(text)],
                styles=[
                    Style(
                        text_decoration="underline",
                        font_size="1.2rem",
                        font_family="Syne Mono",
                    )
                ],
                attrs={"target": "_blank"},
            )
        ],
    )
