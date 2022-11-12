from pyfyre.nodes import *
from widgets import (
    Section,
    MainSection,
    dialog_text,
    image,
    user_action,
    HeaderSection,
)


class About(MainSection):  # type: ignore[misc]
    def build(self) -> list[Node]:
        return [
            HeaderSection("About Me"),
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
                user_action("/skills", "I want to see your skills.", router=True),
                user_action("/", "You're boring. Take me back.", router=True),
            ),
        ]
