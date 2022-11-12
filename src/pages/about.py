from pyfyre.nodes import *
from components.sections import MainSection, Section, PageTitle
from components.clickables import RouterButton
from components.contents import image, dialog_text


class About(MainSection):
    def build(self) -> list[Node]:
        return [
            PageTitle("About Me"),
            Section(
                image(
                    "https://media.tenor.com/WbqsQXRTsawAAAAC"
                    "/anya-spy-x-family-anime-spy-x-family-anya.gif"
                ),
                dialog_text("I'm kinda cool you know ✨"),
                dialog_text(
                    "I am a self-taught programmer and an aspiring game developer. "
                    "Currently (hatefully) studying as a computer science student."
                ),
                dialog_text("That's all I want to say for now (⁠~⁠￣⁠~⁠￣⁠)⁠~"),
                RouterButton("I want to see your skills.", "/skills"),
                RouterButton("You're boring. Take me back.", "/"),
            ),
        ]
