from pyfyre import State

show_about_link_on_home_page = State[bool](False)
nav_is_opened = State[bool](False)
surprise_message_states = {
    "is_active": State[bool](False),
    "timeout": None,
    "text": "",
}
