import App_Matplotlib
import PySimpleGUI as sg
import matplotlib.pyplot as plt

layout = [[sg.Text("Insert a country:"),sg.InputText(do_not_clear=False)]
    ,[sg.Button('Plot'), sg.Cancel(), sg.Button('Popup')]]

window = sg.Window('Have some Matplotlib....', layout)

while True:
    event, values = window.read()
    if event in (sg.WIN_CLOSED, 'Cancel'):
        break
    elif event == 'Plot':
        if App_Matplotlib.plot_country_cases(values[0])=="not a valid country":
            sg.Popup("Not a valid country")
        else: App_Matplotlib.plot_country_cases(values[0])
    elif event == 'Popup':
        sg.popup("Yes, your application is still running")
window.close()