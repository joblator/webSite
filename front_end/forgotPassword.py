from nicegui import ui
from requests import get
from fastapi import status
import re
from yagmail import SMTP

def send_email(email):
    response = get(f'http://127.0.0.1:8090/user/{email}')
    if response.status_code == status.HTTP_404_NOT_FOUND:
        ui.notify('Email not registered', color='negative')
        return
    if response.status_code != status.HTTP_200_OK:
        ui.notify('Server error, try again later', color='negative')
        return

    user = response.json()
    password = user.get('password')
    if not password:
        ui.notify('No password is stored for this user', color='negative')
        return

    conn = SMTP('tiulwebsite@gmail.com', oauth2_file='secret.json')
    conn.send(
        to=email,
        subject='Password recovery',
        contents=[
            f'Hello {user.get("name", "user")},',
            'You requested password recovery.',
            f'Your current password is: {password}',
            'Please keep it secure.'
        ]
    )
    ui.notify('Password sent to your email', color='positive')


@ui.page('/password')
def password_page():
    EMAIL_REGEX = re.compile(r'^[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}$')
    with ui.row().classes('w-full justify-center gap-10'):
        ui.label('Recover password').classes('text-red-500 text-5xl')
    with ui.row().classes('w-full justify-center gap-10'):
        email = ui.input(placeholder='Enter your email', validation={'Invalid email format': lambda v: EMAIL_REGEX.match(v) is not None})
    with ui.row().classes('w-full justify-center gap-10'):
        ui.button('Recover', on_click=lambda: send_email(email.value))