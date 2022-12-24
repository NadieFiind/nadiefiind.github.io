from pyfyre import Style
from pyfyre.nodes import *
from components import social_links
from components.sections import MainSection, PageTitle, Section
from components.contents import text


class Services(MainSection):
    def build(self) -> list[Node]:
        return [
            PageTitle("My Services"),
            Section(
                text(
                    "I'm currently not listing any of my services as I am still "
                    "not very confident with my skills. But if you really want to "
                    "hire me, you can contact me for details."
                ),
                styles=[Style(margin_bottom="30px")],
            ),
            Section(social_links()),
        ]
