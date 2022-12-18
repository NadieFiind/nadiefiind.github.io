from pyfyre.nodes import *
from components import social_links
from components.sections import MainSection, PageTitle, Section
from components.contents import small_text


class Services(MainSection):
    def build(self) -> list[Node]:
        return [
            PageTitle("My Services"),
            Section(small_text("Coming soon...")),
            Section(social_links()),
        ]
