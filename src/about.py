from pyfyre.nodes import *
from widgets import Section, MainSection
from styles import head_style


class About(MainSection):  # type: ignore[misc]
    def build(self) -> list[Node]:
        return [
            Section(
                Element("h2", lambda: [Text("About Me")], styles=[head_style]),
                tag_name="header",
            )
        ]
