from typing import Any, Callable
from pyfyre import render, Style
from pyfyre.nodes import *
from pages import Home, About, Skills, Projects
from components import Background, Nav, SurpriseMessage


def page_builder(main: Element) -> Callable[[Any], Element]:
    def route_builder(arg: Any) -> Element:
        return Element(
            "div",
            lambda: [
                Background(),
                main,
                Nav(),
                SurpriseMessage(),
                Link(
                    "https://twitter.com/adityar51253736/status/1584827745112317953"
                    "?t=0518MJBJHHmQZxub23fPhA&s=19",
                    lambda: [Text("Background Source")],
                    styles=[
                        Style(
                            position="fixed",
                            bottom="0",
                            font_family="Syne Mono",
                            opacity="0.5",
                            font_size="1rem",
                            z_index="2000",
                        )
                    ],
                    attrs={"target": "_blank"},
                ),
            ],
        )

    return route_builder


render(
    {
        "/": page_builder(Home()),
        "/about": page_builder(About()),
        "/skills": page_builder(Skills()),
        "/projects": page_builder(Projects()),
    }
)
