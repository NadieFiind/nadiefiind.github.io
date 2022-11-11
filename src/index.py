from pyfyre import render, Style
from pyfyre.nodes import *
from home import Home


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


class HomePage(Widget):
    def build(self) -> list[Node]:
        return [Background(), Home()]


render({"/": lambda: HomePage()})
