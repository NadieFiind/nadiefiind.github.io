from typing import Type, Any, Callable
from pyfyre import render, Style
from pyfyre.nodes import *
from components import Background, crypto_addresses
from pages import Home, Services


def page_builder(main: Type[Widget]) -> Callable[[Any], Element]:
    def route_builder(arg: Any) -> Element:
        return Element(
            "div",
            lambda: [
                Background(),
                main(),
                Link(
                    "https://twitter.com/adityar51253736/status/1584827745112317953"
                    "?t=0518MJBJHHmQZxub23fPhA&s=19",
                    lambda: [Text("Background by Aditya")],
                    styles=[
                        Style(
                            position="fixed",
                            bottom="0",
                            right="5px",
                            font_family="Syne Mono",
                            opacity="0.5",
                            font_size="1rem",
                            z_index="2000",
                        )
                    ],
                    attrs={"target": "_blank"},
                ),
                *crypto_addresses(),
            ],
        )

    return route_builder


render(
    {
        "/": page_builder(Home),
        "/services": page_builder(Services),
    }
)
