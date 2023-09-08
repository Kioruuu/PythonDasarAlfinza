import PySimpleGUI as sg 

layout = [[sg.Button('Klik Saya')]]

window = sg.Window('Contoh program PySimpleGUI', layout)

while True:
    event, values = window.read()
    if event == sg.WINDOW_CLOSED:
        break
    elif event == 'Klik Saya':
        print('tombol di klik')

    window.close()