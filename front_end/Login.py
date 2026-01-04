from nicegui import ui,app
import Login as Login
import mainPage as mainPage
import SignUp as SignUp
import addTour as addTour
import forgotPassword as forgotPassword
import re
from requests import post
from fastapi import status
def click_logIn(email,password):
    data ={"email": email,"password": password}
    response = post('http://127.0.0.1:8090/user/login',json=data) 
    if response.status_code == status.HTTP_200_OK:
        app.storage.user.update({"user_id":response.json()['_id']})
        app.storage.user.update({"is_admin":response.json()['is_admin']})
        ui.navigate.to('/mainPage')
    elif response.status_code == status.HTTP_404_NOT_FOUND:
        ui.notify("invalid data")
def click_signUp():
    ui.navigate.to('/signUp')
def click_password():
    ui.navigate.to('/password')
@ui.page('/')
def users_page():
    EMAIL_REGEX = re.compile(r'^[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}$')
    with ui.row().classes("w-full justify-center gap-10"):
        with ui.column():
            ui.label("Log in").classes('text-red-500 text-5xl')
            email = ui.input(placeholder="Enter your email",validation={"Invalid email format": lambda v: EMAIL_REGEX.match(v) is not None,})
            password = ui.input(placeholder="Enter your password",password=True,password_toggle_button=True)
    with ui.row().classes("w-full justify-center gap-10"):
        ui.button('Sign up', on_click=click_signUp)
        ui.button('Log in',on_click=lambda: click_logIn(email.value,password.value))
        ui.button("forgot Password", on_click=click_password)
    
ui.run(storage_secret="RIPkirk67")