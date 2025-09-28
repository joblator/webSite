from nicegui import ui
with ui.row().classes("w-full justify-center gap-10"):
    with ui.column():
        ui.label("Log in").classes('text-red-500 text-5xl')
        ui.input(placeholder="Enter your first name")
        ui.input(placeholder="Enter your last name")
        ui.number(label ="Enter your age",value= 0,validation={"Age needs to be between 0 and 120": lambda value: 0 < value < 120})        
with ui.row().classes("w-full justify-center gap-10"):
    ui.button('Sign up', on_click=lambda: ui.notify('You are now signed up!'))
    ui.button('Log in',)

ui.run()