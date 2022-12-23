from typing import Any, Optional
from pyfyre import Style
from pyfyre.nodes import *
from styles import title_style


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
        styles=[Style(width=width)],
    )


def strong_text(text: Any, **kwargs: Any) -> Element:
    style = Style(font_family="Syne Mono", font_weight="bold", font_size="1.2rem")
    if kwargs.get("styles"):
        kwargs["styles"].insert(0, style)
    else:
        kwargs["styles"] = [style]

    return Element(
        "p", lambda: [text if isinstance(text, Element) else Text(text)], **kwargs
    )


def text(text: Any, **kwargs: Any) -> Element:
    style = Style(font_family="Poppins", font_size="1rem")

    if kwargs.get("styles"):
        kwargs["styles"].insert(0, style)
    else:
        kwargs["styles"] = [style]

    return Element(
        "p", lambda: [text if isinstance(text, Element) else Text(text)], **kwargs
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
