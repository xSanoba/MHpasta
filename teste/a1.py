import PySimpleGUI as sg
from a2 import registro
sg.theme ("LightBlue5")

def Login():
    layout = [  [sg.Text("Email :")], [sg.InputText()],
                [sg.Text("Senha :")], [sg.InputText()],
                [sg.Text("Cpf :")], [sg.InputText()],
                [sg.Button('Login'), sg.Button('Registro')] ]
    # Nome da janela
    window = sg.Window('Login', layout)

    # Loop para processar “eventos” e obter os “valores” das entradas
    while True:
        event, values = window.read()

        # se o usuário clicar em Registrarse
        if event == sg.WIN_CLOSED or event == 'Cancel':
            break
        if event == 'Registro' :
                window.close()
                registro()       
    window.close()
    
Login()