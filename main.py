from nicegui import ui
ui.input(placeholder="Enter your first name")
ui.input(placeholder="Enter your last name")
ui.number(label ="Enter your age",value= 0,validation={"Age needs to be between 0 and 120": lambda value: 0 < value < 120})
ui.input(placeholder="Enter your email",validation={"need to contain @gmail.com": lambda value: "@gmail.com" in value})
ui.input(placeholder="Enter your password",password=True,password_toggle_button=True)
ui.input(placeholder="Enter your password again")
with ui.dropdown_button('Select your gender', auto_close=True):
    ui.item('Male', on_click=lambda: ui.notify('You clicked Male'))
    ui.item('Female', on_click=lambda: ui.notify('You clicked Female'))
    ui.item('Other', on_click=lambda: ui.notify('You clicked Other'))
    
ui.button('Sign in', on_click=lambda: ui.notify('You are now signed in!'))

ui.run()
