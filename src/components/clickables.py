from typing import Any, Callable
from browser import DOMEvent, window
from pyfyre import Style
from pyfyre.nodes import *
from styles import center_y


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
        lname = self.name.lower()

        def icon() -> Element:
            if lname == "gravatar":
                return Element("i", attrs={"class": "fa-solid fa-user"})
            elif lname == "email":
                return Element("i", attrs={"class": "fa-solid fa-envelope"})
            elif lname == "ko-fi":
                return Element("i", attrs={"class": "fa-solid fa-mug-hot"})
            elif lname == "pypi":
                return Element("i", attrs={"class": "fa-brands fa-python"})
            elif lname == "top-gg":
                return Element(
                    "img",
                    attrs={
                        "src": "https://cdn.discordapp.com/attachments/"
                        "1031379767674556436/1055756180078731325/34552786.png"
                    },
                    styles=[center_y, Style(width="2.5rem", filter="invert(100%)")],
                )
            elif lname == "hoyolab":
                return Element(
                    "img",
                    attrs={
                        "src": "https://cdn.discordapp.com/attachments/10313797"
                        "67674556436/1040654731049181285/hoyolab.png"
                    },
                    styles=[center_y, Style(height="2.5rem")],
                )
            elif lname == "tradersync":
                return Element("i", attrs={"class": "fa-solid fa-chart-column"})

            return Element("i", attrs={"class": f"fa-brands fa-{lname}"})

        return [Link(self.url, lambda: [icon()], attrs={"target": "_blank"})]


def internal_link(text: Any, route: str) -> Element:
    return RouterLink(
        route,
        lambda: [Text(text)],
        styles=[Style(color="#8987f3", text_decoration="underline")],
        attrs={"target": "_blank"},
    )


def external_link(text: Any, url: str) -> Element:
    return Link(
        url,
        lambda: [Text(text)],
        styles=[Style(color="#8987f3", text_decoration="underline")],
        attrs={"target": "_blank"},
    )
