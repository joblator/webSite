from nicegui import ui,app
from fastapi import status
from requests import post,put,get
from datetime import datetime
from threading import Thread 
from asyncio import sleep

file_data = None

file_data = None

async def upload_file(username):
    file_name = file_data.name
    file_content = await file_data.read()  # Reads the content as bytes
    content_type = file_data.content_type
    
    put('http://127.0.0.1:8090/tour/file/'+username,
        files = {"file": (file_name , file_content, content_type)})
    
def update_file(event):
    global file_data
    file_data = event.file

async def update_the_tour(id,description,like,favorite,location,tourMaker):
    data = {"_id": id, "description": description, "like": like,"favorite": favorite,"location": location,"tourMaker":tourMaker}
    
    result = put('http://127.0.0.1:8090/tour',json=data)

    if result.status_code == status.HTTP_200_OK:
        ui.notify('updates saved')
        # add the profile image for the user
        if file_data != None:
            ui.notify('please wait while uploading the file...')
            await upload_file(id)
            ui.navigate.to('/mainPage')            
    else:
        ui.notify('invalid data') 
 


        

@ui.page('/editTour/{tour_id}',title="Update user")
def update_user(tour_id: str):
    ui.image('http://127.0.0.1:8090/tour/file/'+tour_id).classes('w-10')
    result = get('http://127.0.0.1:8090/tour/'+tour_id)
    with ui.card().classes('absolute-center'):
        with ui.column():
            des_input = ui.input('description')
            with ui.row().classes('items-center gap-2'):
                ui.label('like')
                like_input = ui.toggle({True:"True", False:"False"},value=False)
            with ui.row().classes('items-center gap-2'):
                ui.label('favorite')
                fav_input = ui.toggle({True:"True", False:"False"},value=False)
            location_input = ui.input('location')
            ui.image('http://127.0.0.1:8090/tour/file/'+tour_id).classes('w-10')
            file_input = ui.upload(label="Profile image",on_upload=lambda e: update_file(e)).classes('max-w-full')
            ui.button('OK',on_click=lambda:update_the_tour(tour_id,des_input.value,like_input.value,fav_input.value,location_input.value,result.json()["tourMaker"])).classes('w-full')
    # fill all the data for the user
    des_input.set_value(result.json()["description"])
    like_input.set_value(result.json()["like"])
    fav_input.set_value(result.json()["favorite"])
    location_input.set_value(result.json()["location"])
