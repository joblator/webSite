from nicegui import ui
import re
@ui.page('/password')
def password_page():
    EMAIL_REGEX = re.compile(r'^[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}$')
    with ui.row().classes("w-full justify-center gap-10"):
        ui.label("Recover password").classes('text-red-500 text-5xl')
    with ui.row().classes("w-full justify-center gap-10"):
        ui.input(placeholder="Enter your email",validation={"Invalid email format": lambda v: EMAIL_REGEX.match(v) is not None,})
    with ui.row().classes("w-full justify-center gap-10"):
        ui.button('Recover', on_click=lambda: ui.notify('Email sent'))