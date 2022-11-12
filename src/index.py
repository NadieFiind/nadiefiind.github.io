from pyfyre import render
from pyfyre.nodes import *
from widgets import Background
from home import Home
from about import About
from skills import Skills


class HomePage(Widget):
    def build(self) -> list[Node]:
        return [Background(), Home()]


class AboutPage(Widget):
    def build(self) -> list[Node]:
        return [Background(), About()]


class SkillsPage(Widget):
    def build(self) -> list[Node]:
        return [Background(), Skills()]


render(
    {
        "/": lambda: HomePage(),
        "/about": lambda: AboutPage(),
        "/skills": lambda: SkillsPage(),
    }
)
