from typing import Any, Optional
from pyfyre import Style
from pyfyre.nodes import *
from styles import mq_mobile, centerx, centery, debug


class Background(Widget):
    def __init__(self) -> None:
        super().__init__(
            styles=[
                Style(
                    width="100vw",
                    height="100vh",
                    position="fixed",
                    z_index="-1000",
                )
            ],
        )

    def build(self) -> list[Node]:
        return [
            Element(
                "img",
                attrs={"src": "/images/space_background.jpg"},
                styles=[Style(height="100vh", opacity="0.5")],
            )
        ]


class MainSection(Widget):
    def __init__(self) -> None:
        super().__init__(
            tag_name="main", states=[mq_mobile], styles=[Style(padding_top="50px")]
        )

    def build(self) -> list[Node]:
        return []


class Section(Widget):
    def __init__(self, *views: Node, tag_name: str = "section", **kwargs: Any) -> None:
        self.views = views

        additional_styles = kwargs.get("styles")
        if additional_styles is None:
            additional_styles = []
        else:
            del kwargs["styles"]

        super().__init__(
            tag_name=tag_name,
            styles=[
                centerx,
                debug,
                Style(
                    width="calc(100vw / 1.3)" if mq_mobile.matches else "200px",
                    margin_bottom="40px",
                    text_align="center",
                ),
            ]
            + additional_styles,
            **kwargs,
        )

    def build(self) -> list[Node]:
        return [*self.views]


class SocMedLink(Widget):
    def __init__(self, name: str, url: str, **kwargs: Any) -> None:
        self.name = name
        self.url = url
        super().__init__(styles=[Style(font_size="2.5rem", margin="0 10px")], **kwargs)

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
                    styles=[centery, Style(height="2.5rem")],
                )

            return Element("i", attrs={"class": f"fa-brands fa-{self.name.lower()}"})

        return [Link(self.url, lambda: [icon()], attrs={"target": "_blank"})]


def glowing_circle_image(url: str, *, height: Optional[str] = None) -> Element:
    return Element(
        "img",
        attrs={
            "src": url,
            "class": "glowing-circle" if not mq_mobile.matches else "",
        },
        styles=[Style(border_radius="100%", height=height or "auto")],
    )


def image(url: str) -> Element:
    return Element("img", attrs={"src": url}, styles=[centerx])


def dialog_text(text: Any) -> Element:
    return Element(
        "p",
        lambda: [Text(text)],
        styles=[
            Style(font_family="Schoolbell", font_size="1.5rem", margin="20px auto")
        ],
    )


def user_action(onclick: Any, text: Any, *, router: bool = False) -> Element:
    styles = [
        Style(
            font_size="1.3rem",
            font_family="Syne Mono",
            text_decoration="underline" if mq_mobile.matches else "none",
        )
    ]
    attrs = {"class": "glowing" if not mq_mobile.matches else ""}

    if router:
        return RouterLink(onclick, lambda: [Text(text)], styles=styles, attrs=attrs)

    return Button(onclick, lambda: [Text(text)], styles=styles, attrs=attrs)
