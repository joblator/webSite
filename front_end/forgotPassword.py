from nicegui import ui
import re
from yagmail import SMTP
def send_email(email):
    conn = SMTP('tiulwebsite@gmail.com',oauth2_file='client.json')
    conn.send(to=email ,subject="test subject",contents="test content")
@ui.page('/password')
def password_page():
    EMAIL_REGEX = re.compile(r'^[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}$')
    with ui.row().classes("w-full justify-center gap-10"):
        ui.label("Recover password").classes('text-red-500 text-5xl')
    with ui.row().classes("w-full justify-center gap-10"):
        email = ui.input(placeholder="Enter your email",validation={"Invalid email format": lambda v: EMAIL_REGEX.match(v) is not None,})
    with ui.row().classes("w-full justify-center gap-10"):
        ui.button('Recover', on_click=lambda:send_email(email.value))