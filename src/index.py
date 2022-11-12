from pyfyre import render
from pyfyre.nodes import *
from widgets import Background, Nav
from pages import Home, About, Skills, Projects


class HomePage(Widget):
    def build(self) -> list[Node]:
        return [Background(), Home(), Nav()]


class AboutPage(Widget):
    def build(self) -> list[Node]:
        return [Background(), About(), Nav()]


class SkillsPage(Widget):
    def build(self) -> list[Node]:
        return [Background(), Skills(), Nav()]


class ProjectsPage(Widget):
    def build(self) -> list[Node]:
        return [Background(), Projects(), Nav()]


render(
    {
        "/": lambda: HomePage(),
        "/about": lambda: AboutPage(),
        "/skills": lambda: SkillsPage(),
        "/projects": lambda: ProjectsPage(),
    }
)
