from pyfyre.nodes import *
from widgets import (
    Section,
    MainSection,
    dialog_text,
    image,
    HeaderSection,
    title,
    external_link,
)


class Projects(MainSection):  # type: ignore[misc]
    def build(self) -> list[Node]:
        return [
            HeaderSection("My Projects"),
            Section(
                image("https://avatars.githubusercontent.com/u/81043230?s=280&v=4"),
                title("PyFyre"),
                dialog_text(
                    "An open-source Python web frontend framework for "
                    "building reactive web user interfaces.",
                    serious=True,
                ),
                external_link("https://pypi.org/project/pyfyre", "PyPI"),
                external_link("https://github.com/pyfyre/pyfyre", "Repository"),
                external_link("https://pyfyre-docs.netlify.app", "Documentation"),
                external_link(
                    "https://www.facebook.com/pyfyreframework", "Facebook Page"
                ),
                external_link("https://discord.gg/YzEDuqhgZJ", "Discord Server"),
            ),
        ]
