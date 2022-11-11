from pyfyre import render
from pyfyre.nodes import *
from widgets import Background
from home import Home
from about import About


class HomePage(Widget):
    def build(self) -> list[Node]:
        return [Background(), Home()]


class AboutPage(Widget):
    def build(self) -> list[Node]:
        return [Background(), About()]


render(
    {
        "/": lambda: HomePage(),
        "/about": lambda: AboutPage(),
    }
)
