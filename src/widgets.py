from browser import document, timer
from typing import Any, Optional
from pyfyre import Style, State
from pyfyre.nodes import *
from styles import mq_mobile, centerx, centery, debug, head_style

nav_is_opened = State[bool](False)


class Nav(Widget):
    def __init__(self) -> None:
        super().__init__(
            styles=[
                Style(
                    width="100%",
                    position="fixed",
                    z_index="10000",
                    top="0",
                    background_color="#0009",
                    transition="ease 0.5s",
                    padding_left="20px",
                )
            ],
            states=[nav_is_opened],
        )

    def build(self) -> list[Node]:
        if nav_is_opened.value:
            self.style.update(right="0")
        else:
            self.style.update(right="-100%")

        return [
            Button(
                lambda ev: nav_is_opened.set_value(not nav_is_opened.value),
                styles=[
                    Style(
                        position="fixed",
                        border_radius="100%",
                        width="50px",
                        height="50px",
                        top="7.5px",
                        right="7.5px",
                        background_image="url(/images/avatar.png)",
                        background_size="cover",
                    ),
                ],
            ),
            user_action("/", "Home", router=True),
            user_action("/about", "About", router=True),
            user_action("/skills", "Skills", router=True),
            user_action("/projects", "Projects", router=True),
        ]


class Background(Widget):
    def __init__(self) -> None:
        super().__init__(
            styles=[
                Style(
                    width="100vw",
                    height="100vh",
                    position="fixed",
                    z_index="-1000",
                    background_image="url(/images/background.jpg)",
                    background_size="cover",
                    background_position="center",
                    opacity="0.5",
                )
            ],
        )

    def build(self) -> list[Node]:
        return [
            Link(
                "https://twitter.com/adityar51253736/status/1584827745112317953"
                "?t=0518MJBJHHmQZxub23fPhA&s=19",
                lambda: [Text("Background Source")],
                styles=[
                    Style(position="absolute", bottom="0", font_family="Syne Mono")
                ],
                attrs={"target": "_blank"},
            )
        ]


class MainSection(Widget):
    def __init__(self, **kwargs: Any) -> None:
        additional_states = kwargs.get("states")
        if additional_states is None:
            additional_states = []
        else:
            del kwargs["states"]

        super().__init__(
            tag_name="main",
            states=[mq_mobile] + additional_states,
            styles=[Style(padding_top="50px")],
            **kwargs,
        )

    def build(self) -> list[Node]:
        return []


class Section(Widget):
    def __init__(self, *views: Node, tag_name: str = "section", **kwargs: Any) -> None:
        self.views = views

        additional_styles = kwargs.get("styles")
        if additional_styles is None:
            additional_styles = []
        else:
            del kwargs["styles"]

        super().__init__(
            tag_name=tag_name,
            styles=[
                centerx,
                debug,
                Style(
                    width="calc(100vw / 1.3)" if mq_mobile.matches else "200px",
                    margin_bottom="40px",
                    text_align="center",
                ),
            ]
            + additional_styles,
            **kwargs,
        )

    def build(self) -> list[Node]:
        return [*self.views]


class HeaderSection(Section):
    def __init__(self, title: Any, **kwargs: Any) -> None:
        super().__init__(
            Element("h2", lambda: [Text(title)], styles=[head_style]),
            tag_name="header",
            **kwargs,
        )


class SocMedLink(Widget):
    def __init__(self, name: str, url: str, **kwargs: Any) -> None:
        self.name = name
        self.url = url
        super().__init__(styles=[Style(font_size="2.5rem", margin="0 10px")], **kwargs)

    def build(self) -> list[Node]:
        def icon() -> Element:
            if self.name.lower() == "email":
                return Element("i", attrs={"class": "fa-solid fa-envelope"})
            elif self.name.lower() == "hoyolab":
                return Element(
                    "img",
                    attrs={
                        "src": "https://cdn.discordapp.com/attachments/10313797"
                        "67674556436/1040654731049181285/hoyolab.png"
                    },
                    styles=[centery, Style(height="2.5rem")],
                )

            return Element("i", attrs={"class": f"fa-brands fa-{self.name.lower()}"})

        return [Link(self.url, lambda: [icon()], attrs={"target": "_blank"})]


def image(url: str, *, width: str = "auto", label: Optional[Any] = None) -> Element:
    children: list[Node] = []
    children.append(Element("img", attrs={"src": url}, styles=[Style(width="100%")]))

    if label:
        children.append(
            Element(
                "p",
                lambda: [Text(label)],
                styles=[
                    head_style,
                    Style(
                        font_size="1rem",
                        margin="10px auto 40px auto",
                    ),
                ],
            )
        )

    return Element("div", lambda: children, styles=[Style(width=width)])


def dialog_text(text: Any, *, serious: bool = False) -> Element:
    return Element(
        "p",
        lambda: [Text(text)],
        styles=[
            Style(
                font_family="Schoolbell" if not serious else "Sans",
                font_size="1.5rem" if not serious else "1.3rem",
                margin="20px auto",
            )
        ],
    )


def user_action(onclick: Any, text: Any, *, router: bool = False) -> Element:
    styles = [
        Style(
            font_size="1.3rem",
            font_family="Syne Mono",
            text_decoration="underline",
        )
    ]
    child: Element

    if router:
        child = RouterLink(onclick, lambda: [Text(text)], styles=styles)
    else:
        child = Button(onclick, lambda: [Text(text)], styles=styles)

    return Element(
        "div",
        lambda: [child],
        styles=[Style(margin="20px auto")],
    )


def title(title: Any, **kwargs: Any) -> Element:
    return Element(
        "h3",
        lambda: [Text(title)],
        styles=[
            head_style,
            Style(
                font_size="2rem",
                margin="20px auto",
            ),
        ],
        **kwargs,
    )


def item_list(items: list[Any], *, title: Optional[Any] = None) -> Element:
    children: list[Node] = (
        [
            Element(
                "p",
                lambda: [Text(title)],
                styles=[
                    head_style,
                    Style(
                        font_size="1.5rem",
                        margin="10px auto",
                    ),
                ],
            )
        ]
        if title
        else []
    )
    children += map(
        lambda item: Element(
            "li",
            lambda: [Text(item)],
            styles=[
                Style(
                    font_family="Poppins",
                    font_size="1.2rem",
                    list_style_type="circle",
                    margin_bottom="5px",
                )
            ],
        ),
        items,
    )

    return Element(
        "ul",
        lambda: children,
        styles=[Style(margin="20px auto", list_style_position="inside")],
    )


_huge_toast_timeout = None


def huge_toast(message: str) -> None:
    global _huge_toast_timeout

    el = document.select_one(".huge-toast")
    el.textContent = message

    if el.classList.contains("active"):
        timer.clear_timeout(_huge_toast_timeout)
    else:
        el.classList.add("active")

    _huge_toast_timeout = timer.set_timeout(lambda: el.classList.remove("active"), 100)


def external_link(url: str, text: Any) -> Element:
    return Element(
        "div",
        lambda: [
            Link(
                url,
                lambda: [Text(text)],
                styles=[
                    Style(
                        text_decoration="underline",
                        font_size="1.2rem",
                        font_family="Syne Mono",
                    )
                ],
                attrs={"target": "_blank"},
            )
        ],
    )
