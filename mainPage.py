from nicegui import ui
import random
image_list =["desert.webp","desert2.webp","desert3.webp","desert4.webp"]
index_list = []
@ui.refreshable
def show_card():
    ui.label(len(index_list))
    with ui.card().tight():
        ui.image(image_list[len(index_list)-1])
        with ui.card_section():
            ui.label('this is a tour of the desert')
            ui.chip('favorites', selectable=True, icon='bookmark', color='red')
            ui.chip('like', selectable=True, icon='favorite', color='blue')
def show_next():
    if len(index_list) < len(image_list) - 1:
        index_list.append(0)
        show_card.refresh()
    else:
        ui.notify("this is the last tiul")
def show_prev():
    if len(index_list) > 0:
        index_list.pop(0)
        show_card.refresh()
    else:
        ui.notify("this is the first tiul")
show_card()
ui.button("show next",on_click=show_next)
ui.button("show prev",on_click=show_prev)        
ui.run()