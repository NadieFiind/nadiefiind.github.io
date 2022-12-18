from pyfyre.nodes import *
from components.sections import MainSection, PageTitle


class Services(MainSection):
    def build(self) -> list[Node]:
        return [PageTitle("My Services")]
