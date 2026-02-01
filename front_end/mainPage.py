from nicegui import ui,app
from requests import get,post,delete
def add_tour():
    data = {
  "description": "string",
  "like": False,
  "favorite": False,
  "location": "string"
}
    result = post('http://127.0.0.1:8090/tour', json=data)
    ui.navigate.to('/editTour/'+result.json()['_id'])
    
def delete_tour(id:str):
    result = delete(f'http://127.0.0.1:8090/tour/{id}')
def fetch_tours(description:str,location:str):
    if description == "":
        result = get('http://127.0.0.1:8090/tour/all')
    else:
        tour_filter = {"description":description,"location":location}
        result = post('http://127.0.0.1:8090/tour/filter',json=tour_filter)
    data = result.json()
    return data
@ui.refreshable
def show_table_content(description:str = "",location:str = ""):
    data = fetch_tours(description,location)   
    with ui.row().classes('flex-wrap gap-4 justify-center'):
        for u in data:
            id = u['_id']   
            with ui.card().classes('w-60 h-80 shadow-md'):
                ui.image('http://127.0.0.1:8090/tour/file/'+u['_id']).classes('w-full h-32 object-cover')
                ui.label(u['description']).classes('font-bold text-sm')
                ui.label(f"ID: {u['_id']}").classes('text-xs text-gray-500')
                ui.label(f"location:{u['location']}")
                ui.button(f"edit tour",on_click=lambda currentId = id: ui.navigate.to('/editTour/'+currentId))#use current id so that the lambda copies the value and doesent use the last knows id val
                ui.button(f"delete button",on_click=lambda currentId = id: delete_tour(currentId))
def tour_list_container(description: str = "", like: bool = False):
    data = fetch_tours(description, like)
    
    # The main container card
    with ui.card().classes('absolute-center w-3/4 h-[80vh] overflow-y-auto'):
        # 1. Header (Logo and Title)
        with ui.row().classes('items-center mb-4'):
            ui.button("refresh",on_click=lambda:show_table_content.refresh())
            if app.storage.user.get("is_admin","false"):
                ui.button(f"Add Tour",on_click=add_tour)
            else:
                ui.label(f"welcome {app.storage.user.get("user_id","Guest")} you are not an  admin")
            ui.label('liked').classes('text-3xl')
            button_location = ui.input(label="enter location")
            button_description = ui.input(label="enter description")
            ui.button("search",on_click=lambda:show_table_content.refresh(description=button_description.value,location=button_location.value))
        ui.separator()

        show_table_content()
@ui.page('/mainPage')   
def mainPage_page():
    tour_list_container('',False)

