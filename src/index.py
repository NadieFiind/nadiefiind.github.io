from pyfyre import render
from pyfyre.nodes import *
from widgets import Background
from pages import Home, About, Skills, Projects


class HomePage(Widget):
    def build(self) -> list[Node]:
        return [Background(), Home()]


class AboutPage(Widget):
    def build(self) -> list[Node]:
        return [Background(), About()]


class SkillsPage(Widget):
    def build(self) -> list[Node]:
        return [Background(), Skills()]


class ProjectsPage(Widget):
    def build(self) -> list[Node]:
        return [Background(), Projects()]


render(
    {
        "/": lambda: HomePage(),
        "/about": lambda: AboutPage(),
        "/skills": lambda: SkillsPage(),
        "/projects": lambda: ProjectsPage(),
    }
)
