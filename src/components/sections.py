from abc import ABC
from typing import Any
from pyfyre import Style
from pyfyre.nodes import *
from styles import debug, center_x, title_style


class MainSection(Widget, ABC):
    def __init__(self, **kwargs: Any) -> None:
        style = Style(padding_top="50px")
        if kwargs.get("styles"):
            kwargs["styles"].append(style)
        else:
            kwargs["styles"] = [style]

        super().__init__(tag_name="main", **kwargs)

    def build(self) -> list[Node]:
        return []


class Section(Widget):
    def __init__(self, *nodes: Node, tag_name: str = "div", **kwargs: Any) -> None:
        self.nodes = nodes

        styles = [
            debug,
            center_x,
            Style(
                width="calc(100vw / 1.3)",
                margin_bottom="40px",
                text_align="center",
                max_width="700px",
            ),
        ]
        if kwargs.get("styles"):
            kwargs["styles"] += styles
        else:
            kwargs["styles"] = styles

        super().__init__(tag_name=tag_name, **kwargs)

    def build(self) -> list[Node]:
        return [*self.nodes]


class PageTitle(Section):
    def __init__(self, title: Any, **kwargs: Any) -> None:
        super().__init__(
            Element("h2", lambda: [Text(title)], styles=[title_style]),
            tag_name="header",
            **kwargs,
        )


def title(text: Any, **kwargs: Any) -> Element:
    return Element(
        "h3",
        lambda: [Text(text)],
        styles=[
            title_style,
            Style(
                font_size="2rem",
                margin="20px auto",
            ),
        ],
        **kwargs,
    )
