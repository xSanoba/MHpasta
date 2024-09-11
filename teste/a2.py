import PySimpleGUI as sg
from a1 import Login
def registro():
    # Layout da janela
    layout = [[sg.Text("Nome do prof :")], [sg.InputText()],
            [sg.Text("Email :")], [sg.InputText()],
            [sg.Text("Senha :")], [sg.InputText()],
            [sg.Text("Cpf :")], [sg.InputText()],
            [sg.Button('Registrar-se'), sg.Button('Voltar ao login')]]
    window = sg.Window('Cadastro do usuario', layout)

    while True:
        event, values = window.read()
        if event == sg.WINDOW_CLOSED or event == 'Voltar para Login':
            break
        elif event == 'Registrar-se':
            # Validação dos dados
                sg.popup('Registro realizado com sucesso!')
                Login()
        if event == 'Registrado' :
            window.close()
            import Login
            Login.Login()
        if event == 'Voltar ao login':
            Login()

    window.close()
