from typing import Any, Optional
from pyfyre import Style
from pyfyre.nodes import *
from globals.styles import title_style, center_x


def image(url: str, *, width: str = "auto", label: Optional[Any] = None) -> Element:
    children: list[Node] = []
    children.append(Element("img", attrs={"src": url}, styles=[Style(width="100%")]))

    if label:
        children.append(
            Element(
                "p",
                lambda: [Text(label)],
                styles=[
                    title_style,
                    Style(
                        font_size="1rem",
                        margin="10px auto 40px auto",
                    ),
                ],
            )
        )

    return Element(
        "div",
        lambda: children,
        styles=[
            center_x,
            Style(
                width=width,
                max_width="300px",
            ),
        ],
    )


def dialog_text(text: Any, *, serious: bool = False) -> Element:
    return Element(
        "p",
        lambda: [Text(text)],
        styles=[
            Style(
                font_family="Schoolbell" if not serious else "Sans",
                font_size="1.5rem" if not serious else "1.3rem",
                margin="20px auto",
            )
        ],
    )


def item_list(items: list[Any], *, title: Optional[Any] = None) -> Element:
    children: list[Node] = (
        [
            Element(
                "p",
                lambda: [Text(title)],
                styles=[
                    title_style,
                    Style(
                        font_size="1.5rem",
                        margin="10px auto",
                    ),
                ],
            )
        ]
        if title
        else []
    )
    children += map(
        lambda item: Element(
            "li",
            lambda: [Text(item)],
            styles=[
                Style(
                    font_family="Poppins",
                    font_size="1.2rem",
                    list_style_type="circle",
                    margin_bottom="5px",
                )
            ],
        ),
        items,
    )

    return Element(
        "ul",
        lambda: children,
        styles=[Style(margin="20px auto", list_style_position="inside")],
    )