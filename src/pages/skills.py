from browser import DOMEvent, document
from pyfyre import Style, State
from pyfyre.nodes import *
from globals import surprise_message
from components.sections import MainSection, Section, PageTitle, title
from components.clickables import RouterButton, ActionButton
from components.contents import image, item_list, dialog_text


class Skills(MainSection):
    def __init__(self) -> None:
        self.show_true_skills = State[bool](False)
        super().__init__(states=[self.show_true_skills])

    def build(self) -> list[Node]:
        def show_true_skills(event: DOMEvent) -> None:
            self.show_true_skills.set_value(True)
            surprise_message.show("nope")
            document.select_one("#real-skills").scrollIntoView({"behavior": "smooth"})

        children = [
            PageTitle("My Skills"),
            Section(
                image("https://media.tenor.com/-q4cAjceIqkAAAAC/hololive-calliope.gif"),
                item_list(
                    [
                        "I can identify the sexuality of a cat just by looking at it. "
                        "(or maybe it's nothing really special)",
                        "I can make different meow noises and talk with cats. "
                        "(they often just ignore me)",
                        "I can read Japanese characters a little bit. (what a weeb)",
                        "I can still do well in my classes without studying. (I'm not sure how)",
                    ],
                    title="Summary",
                ),
                ActionButton(show_true_skills, "... That's it?"),
                RouterButton(
                    "Show me the projects that you've worked on.", "/projects"
                ),
            ),
        ]

        if self.show_true_skills.value:
            children.append(
                Section(
                    title("Computer Programming", attrs={"id": "real-skills"}),
                    dialog_text(
                        "Languages, frameworks, and libraries that I often use.",
                        serious=True,
                    ),
                    Element(
                        "div",
                        lambda: [
                            image(
                                "https://cdn.jsdelivr.net/npm/@programming-"
                                "languages-logos/python@0.0.0/python.png",
                                width="40%",
                                label="Python",
                            ),
                            image(
                                "https://upload.wikimedia.org/wikipedia/commons/9/"
                                "99/Unofficial_JavaScript_logo_2.svg",
                                width="40%",
                                label="JavaScript",
                            ),
                            image(
                                "https://upload.wikimedia.org/wikipedia/"
                                "commons/8/80/HTML5_logo_resized.svg",
                                width="40%",
                                label="HTML",
                            ),
                            image(
                                "https://upload.wikimedia.org/wikipedia/commons/thumb/"
                                "d/d5/CSS3_logo_and_wordmark.svg/363px-CSS3_logo_and_wordmark.svg.png",
                                width="40%",
                                label="CSS",
                            ),
                            image(
                                "https://avatars.githubusercontent.com/u/1609975?s=200&v=4",
                                width="40%",
                                label="Dart",
                            ),
                            image(
                                "https://upload.wikimedia.org/wikipedia/commons/7/7e/"
                                "Ren%E2%80%99Py_Logo_6-13-6_200x307px.png",
                                width="40%",
                                label="Ren'Py",
                            ),
                            image(
                                "https://avatars.githubusercontent.com/u/81043230?s=280&v=4",
                                width="40%",
                                label="PyFyre",
                            ),
                            image(
                                "https://cdn.hashnode.com/res/hashnode/image/"
                                "upload/v1615396992718/UBhOk2Nwz.jpeg",
                                width="40%",
                                label="Flask",
                            ),
                            image(
                                "https://opencollective-production.s3.us-west-1"
                                ".amazonaws.com/65ce4980-9d08-11ec-b627-7dcae50745f0.png",
                                width="40%",
                                label="discord.py",
                            ),
                            image(
                                "https://cdn-images-1.medium.com/max/1200/"
                                "1*5-aoK8IBmXve5whBQM90GA.png",
                                width="40%",
                                label="Flutter",
                            ),
                            image(
                                "https://cdathenry.files.wordpress.com/2016"
                                "/11/oslcyof.png?w=172&h=172",
                                width="40%",
                                label="p5.js",
                            ),
                            image(
                                "https://avatars.githubusercontent.com/u/67109815?s=280&v=4",
                                width="40%",
                                label="Tailwind CSS",
                            ),
                        ],
                        styles=[
                            Style(
                                display="flex",
                                flex_wrap="wrap",
                                justify_content="space-around",
                                transform="translateX(-30%)",
                            )
                        ],
                    ),
                    RouterButton(
                        "Show me the projects that you've worked on.", "/projects"
                    ),
                )
            )

        return children
