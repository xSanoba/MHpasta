import PySimpleGUI as sg
from Login import L
def R():
    # Layout da janela
    layout = [[sg.Text("Nome do prof :")], [sg.InputText()],
            [sg.Text("Email :")], [sg.InputText()],
            [sg.Text("Senha :")], [sg.InputText()],
            [sg.Text("Cpf :")], [sg.InputText()],
            [sg.Button('Registrar-se'),]]
    window = sg.Window('Cadastro do usuario', layout)

    while True:
        event, values = window.read()
        if event == sg.WINDOW_CLOSED or event == 'Voltar para Login':
            break
        elif event == 'Registrar-se':
            # Validação dos dados
            if validar_dados(values):
                # Processamento dos dados (salvar no banco de dados, enviar email, etc.)
                salvar_usuario(values)
                sg.popup('Registro realizado com sucesso!')
                Login.L()
        if event == 'Registrado' :
            window.close()
            import Login
            Login.Login()

    window.close()

def validar_dados(values):
    # Implementação da lógica de validação aqui
    # ...
    return True

def salvar_usuario(values):
    pass
    # Implementação da lógica para salvar os dados no banco de dados aqui