from nicegui import ui
import re
from requests import post
from fastapi import status
from datetime import datetime

def logIn_click():
    ui.navigate.to('/')
def signUp_click(username,email,password,admin,dob):
    ui.notify(f"{username},{email},{password},{admin},{dob}")
    data = {"_id":email,"name": username, "dob":datetime.now().strftime("%Y-%m-%d %H:%M:%S"),"is_admin": admin,"password":password}
    response = post('http://127.0.0.1:8090/user',json=data)
    if response.status_code == status.HTTP_200_OK:
        ui.navigate.to('/mainPage')
    elif response.status_code == status.HTTP_404_NOT_FOUND:
        ui.notify("something went wrong")
@ui.page('/signUp')
def signUp_page():
    EMAIL_REGEX = re.compile(r'^[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}$')
    with ui.row().classes("w-full justify-center gap-10"):
        with ui.row().classes("w-full justify-center"):
            ui.label("Sign Up").classes('text-red-500 text-5xl')
            ui.icon("account_circle", color="red").classes('text-5xl')
        with ui.row().classes("w-full justify-center"):
            with ui.column():
                username = ui.input(placeholder="Enter your username")
            with ui.column():
                email = ui.input(placeholder="Enter your email",validation={"Invalid email format": lambda v: EMAIL_REGEX.match(v) is not None,})
                password = ui.input(placeholder="Enter your password",password=True,password_toggle_button=True)
                ui.input(placeholder="Enter your password again",password=True, password_toggle_button=True,validation= {"Not the same as you password":lambda v: password.value == v})
        ui.button('Sign up', on_click=lambda: signUp_click(username.value,email.value,password.value,False,datetime.now()))
        ui.button('Log in',on_click=logIn_click)

