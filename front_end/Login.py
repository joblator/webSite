from nicegui import ui
import front_end.Login as Login
import front_end.mainPage as mainPage
import front_end.SignUp as SignUp
import front_end.addTour as addTour
import front_end.forgotPassword as forgotPassword
def click_logIn():
    ui.navigate.to('/mainPage')
def click_signUp():
    ui.navigate.to('/signUp')
def click_password():
    ui.navigate.to('/password')
@ui.page('/')
def users_page():
    with ui.row().classes("w-full justify-center gap-10"):
        with ui.column():
            ui.label("Log in").classes('text-red-500 text-5xl')
            ui.input(placeholder="Enter your first name")
            ui.input(placeholder="Enter your last name")
            ui.number(label ="Enter your age",value= 0,validation={"Age needs to be between 0 and 120": lambda value: 0 < value < 120})        
    with ui.row().classes("w-full justify-center gap-10"):
        ui.button('Sign up', on_click=click_signUp)
        ui.button('Log in',on_click=click_logIn)
        ui.button("forgot Password", on_click=click_password)
    
ui.run()