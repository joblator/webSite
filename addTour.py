from nicegui import ui
with ui.row().classes("w-full justify-center gap-10"):
    with ui.column():
        ui.input(placeholder="Enter tour description")
        ui.button("add Photo",icon="file_upload")

ui.run()