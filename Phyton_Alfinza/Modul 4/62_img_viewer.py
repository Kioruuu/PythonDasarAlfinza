import PySimpleGUI as sg
import os.path

# First, define the window layout in 2 columns
file_list_column = [
    [sg.Text("Image Folder"), sg.Input(size=(25, 1), enable_events=True, key="-FOLDER-"), sg.FolderBrowse()],
    [sg.Listbox(values=[], enable_events=True, size=(40, 20), key="-FILE LIST-")],
]

# Define the image viewer column
image_viewer_column = [
    [sg.Text("Choose an image from the list on the left:")],
    [sg.Image(key="-IMAGE-")],
    [sg.Text(size=(40, 1), key="-TOUT-")],
]

# Create the full layout
layout = [
    [
        sg.Column(file_list_column),
        sg.VSeparator(),
        sg.Column(image_viewer_column),
    ]
]

# Create the window
window = sg.Window("Image Viewer", layout)

while True:
    event, values = window.read()

    if event == sg.WIN_CLOSED or event == "Exit":
        break

    # If a folder is selected, update the file list
    if event == "-FOLDER-":
        folder = values["-FOLDER-"]
        try:
            # Get a list of files in the folder with allowed extensions
            file_list = [f for f in os.listdir(folder) if os.path.isfile(os.path.join(folder, f)) and
                         f.lower().endswith((".png", ".gif", ".jpg", ".jpeg"))]
        except Exception as e:
            file_list = []

        # Update the file list in the window
        window["-FILE LIST-"].update(file_list)

    # If a file is chosen from the listbox
    elif event == "-FILE LIST-":
        selected_file = values["-FILE LIST-"][0]
        filename = os.path.join(values["-FOLDER-"], selected_file)

        # Update the displayed filename and image
        window["-TOUT-"].update(filename)
        try:
            window["-IMAGE-"].update(filename=filename)
        except Exception as e:
            print("Error updating image:", e)

window.close()
