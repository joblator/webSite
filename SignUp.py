from nicegui import ui
import re
def logIn_click():
    ui.navigate.to('/')
@ui.page('/signUp')
def signUp_page():
    EMAIL_REGEX = re.compile(r'^[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}$')
    with ui.row().classes("w-full justify-center gap-10"):
        with ui.row().classes("w-full justify-center"):
            ui.label("Sign Up").classes('text-red-500 text-5xl')
            ui.icon("account_circle", color="red").classes('text-5xl')
        with ui.row().classes("w-full justify-center"):
            with ui.column():
                ui.input(placeholder="Enter your first name")
                ui.input(placeholder="Enter your last name")
                ui.number(label ="Enter your age",value= 0,validation={"Age needs to be between 0 and 120": lambda value: 0 < value < 120})
            with ui.column():
                ui.input(placeholder="Enter your email",validation={"Invalid email format": lambda v: EMAIL_REGEX.match(v) is not None,})
                password = ui.input(placeholder="Enter your password",password=True,password_toggle_button=True)
                ui.input(placeholder="Enter your password again",password=True, password_toggle_button=True,validation= {"Not the same as you password":lambda v: password.value == v})
                with ui.dropdown_button('Select your gender', auto_close=True) as gender_dropdown:
                    ui.item('Male', on_click=lambda: gender_dropdown.set_text('Male'))
                    ui.item('Female', on_click=lambda: gender_dropdown.set_text('Female'))
                    ui.item('Other', on_click=lambda: gender_dropdown.set_text('Other'))
                    
        ui.button('Sign up', on_click=lambda: ui.notify('You are now signed up!'))
        ui.button('Log in',on_click=logIn_click)

