from nicegui import ui,app
from requests import get,post
def click_tour():
    ui.navigate.to('/addTour')
def fetch_tours(description:str,like:bool):
    if description == "":
        result = get('http://127.0.0.1:8090/tour/all')
    else:
        tour_filter = {"description":description,"location":like}
        result = post('http://127.0.0.1:8090/tour/all',data=tour_filter)
    data = result.json()
    return data
@ui.refreshable
def tour_list_container(description: str = "", like: bool = False):
    data = fetch_tours(description, like)
    
    # The main container card
    with ui.card().classes('absolute-center w-3/4 h-[80vh] overflow-y-auto'):
        # 1. Header (Logo and Title)
        with ui.row().classes('items-center mb-4'):
            if app.storage.user.get("is_admin","false"):
                ui.label(f"welcome {app.storage.user.get("user_id","Guest")} you are an admin")
                ui.button("admin button",on_click=ui.notify("you did something dangerous"))
            else:
                ui.label(f"welcome {app.storage.user.get("user_id","Guest")} you are not an  admin")
            ui.label('liked').classes('text-3xl')
            r = ui.radio(['True', 'false'], value='True')
            ui.label().bind_text_from(r, 'value', backward=lambda v: f'You chose: {v}')
            description = ui.input(placeholder="enter description")
            button = ui.button("search")
            


        # 2. THE FIX: Use ui.row() with flex-wrap instead of ui.column()
        # 'flex-wrap' allows cards to move to the next line
        # 'gap-4' adds space between the cards
        with ui.row().classes('flex-wrap gap-4 justify-center'):
            for u in data:
                # Give each card a fixed width so they align like a grid
                with ui.card().classes('w-60 h-80 shadow-md'):
                    ui.image('http://127.0.0.1:8090/tour/file/'+u['_id']).classes('w-full h-32 object-cover')
                    ui.label(u['description']).classes('font-bold text-sm')
                    ui.label(f"ID: {u['_id']}").classes('text-xs text-gray-500')
@ui.page('/mainPage')   
def mainPage_page():
    tour_list_container('',False)

