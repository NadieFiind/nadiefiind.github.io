from typing import Any
from pyfyre import Style
from pyfyre.nodes import *
from styles import mq_mobile, centerx, debug


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
    def __init__(self, view: Node, *, tag_name: str = "section", **kwargs: Any) -> None:
        self.view = view
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
            ],
            **kwargs,
        )

    def build(self) -> list[Node]:
        return [self.view]


class SocMedLink(Widget):
    def __init__(self, name: str, url: str, **kwargs: Any) -> None:
        self.name = name
        self.url = url
        super().__init__(styles=[Style(font_size="2.5rem", margin="10px")], **kwargs)

    def build(self) -> list[Node]:
        return [
            Link(
                self.url,
                lambda: [
                    Element("i", attrs={"class": f"fa-brands fa-{self.name.lower()}"})
                ],
                attrs={"target": "_blank"},
            )
        ]
