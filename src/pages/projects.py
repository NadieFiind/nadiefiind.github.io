from pyfyre.nodes import *
from components.sections import MainSection, Section, PageTitle, title
from components.clickables import external_link
from components.contents import image, dialog_text


class Projects(MainSection):
    def build(self) -> list[Node]:
        return [
            PageTitle("My Projects"),
            Section(
                image("https://avatars.githubusercontent.com/u/81043230?s=280&v=4"),
                title("PyFyre"),
                dialog_text(
                    "An open-source Python web frontend framework for "
                    "building reactive web user interfaces.",
                    serious=True,
                ),
                dialog_text(
                    "This website is built using PyFyre itself. "
                    "Click the links below for more information about PyFyre",
                    serious=True,
                ),
                external_link("PyPI", "https://pypi.org/project/pyfyre"),
                external_link("Repository", "https://github.com/pyfyre/pyfyre"),
                external_link("Documentation", "https://pyfyre-docs.netlify.app"),
                external_link(
                    "Facebook Page", "https://www.facebook.com/pyfyreframework"
                ),
                external_link("Discord Server", "https://discord.gg/YzEDuqhgZJ"),
            ),
        ]
