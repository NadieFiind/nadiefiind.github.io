from typing import Callable
from pyfyre import render
from pyfyre.nodes import *
from pages import Home, About, Skills, Projects
from components import Background, Nav, SurpriseMessage


def page_builder(main: Element) -> Callable[[], Element]:
    return lambda: Element(
        "div", lambda: [Background(), main, Nav(), SurpriseMessage()]
    )


render(
    {
        "/": page_builder(Home()),
        "/about": page_builder(About()),
        "/skills": page_builder(Skills()),
        "/projects": page_builder(Projects()),
    }
)
