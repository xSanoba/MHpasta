
import PySimpleGUI as sg

def primeira_tela():
    # All the stuff inside your window.
    layout = [  [sg.Text("What's your name?")],
                [sg.InputText(key='nome')],
                [sg.Text(key='mensagem')],
                [sg.Button('Ok'), sg.Button('Cancel'), sg.Button('Outra tela')] ]

    # Create the Window
    window = sg.Window('Hello Example', layout)

    # Event Loop to process "events" and get the "values" of the inputs
    while True:
        event, values = window.read()

        # if user closes window or clicks cancel
        if event == sg.WIN_CLOSED or event == 'Cancel':
            break
        
        if event == 'Outra tela':
            window.close()
            segunda_tela()
        nome = values['nome']
        print(nome)
        window['mensagem'].update(f'{nome}')

        

    window.close()


def segunda_tela():
    # All the stuff inside your window.
    layout = [  [sg.Text("What's your name?")],
                [sg.InputText()],
                [sg.Button('Ok'), sg.Button('Cancel')] ]

    # Create the Window
    window = sg.Window('Hello Example', layout)

    # Event Loop to process "events" and get the "values" of the inputs
    while True:
        event, values = window.read()

        # if user closes window or clicks cancel
        if event == sg.WIN_CLOSED or event == 'Cancel':
            break

        print('Hello', values[0], '!')

    window.close()

primeira_tela()