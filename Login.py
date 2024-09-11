        import PySimpleGUI as sg
sg.theme ("LightBlue5")
def validar():
    alunos = []

    while True:
        layout = [
            [sg.Text('Digite o nome do aluno:')],
            [sg.InputText(key='-NOME-')],
            [sg.Text('Qual é a sua materia: '), sg.Combo(['Portugues','Matematica','Biologia','Quimica','Fisica','Filosofia','Sociologia','Geografia','Historia','Artes','Educação Fisica','Ingles,'],key='lis')], 
            [sg.Text('Digite a primeira nota:')],
            [sg.InputText(key='-NOTA1-')],
            [sg.Text('Digite a segunda nota:')],
            [sg.InputText(key='-NOTA2-')],
            [sg.Button('Adicionar'), sg.Button('Sair'),sg.Button('verlista')]
        ]

        

        window = sg.Window('Cadastro de Alunos', layout)

        while True:
            event, values = window.read()
            window['-NOTA1-'].update(f'')
            window['-NOTA2-'].update(f'')
            window['-NOME-'].update(f'')
            window['lis'].update(f'')
                
            if event == 'Adicionar':
                nome = values['-NOME-']
                n1 = values['-NOTA1-']
                n2 = values['-NOTA2-']
                mat= values['lis']

                
                if nome.isdigit():
                    sg.popup('o nome não pode ser numerico.')
                    continue

                elif values['-NOME-'] =='' and values ['-NOTA1-']=='' and values ['-NOTA2-']=='':
                    sg.popup('não nenhum aluno cadastrado')

                elif len(nome)<3:
                    if nome=='':
                        sg.popup('as informações estao em branco')
                    sg.popup('não existe nome com 3 caracteres ')
                    continue
                elif n1 =='' or n2=='':
                    sg.popup('a informações em branco')
                    continue

                elif n1.replace(".", "", 1).isdigit() and n2.replace(".", "", 1).isdigit():
                    n1 = float(n1)
                    n2 = float(n2)
                    
                    if n1 > 10.0 or n2 > 10.0:
                        sg.popup('O sistema não aceita notas maiores do que 10!')
                    
                    
                    nf = (n1 + n2) / 2
                    
                    if nf >= 8.0:
                        ap = 'A'
                    elif nf >= 6.0:
                        ap = 'B'
                    elif nf >= 4.0:
                        ap = 'C'
                    elif nf >= 2.0:
                        ap = 'D'
                    else:
                        ap = 'E'
                    
                    aluno = {'Nome': nome, 'Nota Final': nf, 'Aproveitamento': ap,'lis': mat}
                    alunos.append(aluno)
                    
                    sg.popup(f'Aluno {nome} adicionado com sucesso!')
                    
                
                else:
                    sg.popup('Ambas as notas devem ser numéricas e positivas.')
            
                
            else:
                break
            if event =='Sair' or event ==sg.WIN_CLOSED :
                break
        if event =='Sair' or event ==sg.WIN_CLOSED :
                break
        if event =='verlista':
            
            if len(alunos)==0:
                sg.popup('não nheum aluno cadastrado')
            else:


                window.close()

                layout = [
                        [sg.Text('Lista de Alunos')],
                        [sg.Multiline(default_text='\n'.join([f"Aluno: {a['Nome']}, Média: {a['Nota Final']}, Aproveitamento: {a['Aproveitamento']},Materia: {a['lis']}" for a in alunos]), size=(60, 20), disabled=True)],
                        [sg.Button('Fechar')]
                    ]

                window = sg.Window('Lista de Alunos', layout)
                event, values = window.read()
                if event in (sg.WIN_CLOSED, 'Fechar'):
                        window.close()
                        break

                if alunos:
                    alunos.sort(key=lambda x: x['Nota Final'], reverse=True)
                    ma = alunos[0]

                    sg.popup(f"Melhor aluno: {ma['Nome']}, Aproveitamento: {ma['Aproveitamento']}")
def cad():
    while True:
        layout = [ [sg.Text('Digite o nome de usuario:')],
                [sg.InputText(key='us')],
                [sg.Text('Digite a sua senha:')],
                [sg.InputText(key='se',password_char='*')],
                [sg.Text('digite um CPF')],
                [sg.InputText(key='CPF')],
                [sg.Text('digite o email')],
                [sg.InputText(key='email')],
                [sg.Button('Finalizar'), sg.Button('Sair')]
                ]
        
        window = sg.Window('cadastro de professores ', layout)
        while True:
            event, values = window.read()
            if event =='Finalizar':
                us=values['us']
                se=values['se']
                em=values['email']
                cpf=values['CPF']
                if us.isdigit():
                        sg.popup('o nome não pode ser numerico.')
                        continue
                elif len(us)<3:
                        if us=='':
                            sg.popup('as informações estao em branco')
                        sg.popup('não existe nome com 3 caracteres ')
                        continue
                if '@' not in em:
                    sg.popup('digite um E-mail valido')
                    continue
                if len(cpf)!=11:
                    sg.popup('o cpf é ivalido precisa 11 digitos')
                    continue
                
                with open('dados_login.txt', 'a') as file:
                    file.write(f'{us},{se}\n')
                sg.popup('você foi cadastrado')
            if event=='Sair':
                break
        if event=='Sair':
            window.close()
            logar()
            
            
            break

    
    
def logar():

    
    
    while True:
        layout = [
            [sg.Text('Digite o nome de usuário:')],
            [sg.InputText(key='-us-')],
            [sg.Text('Digite a sua senha:')],
            [sg.InputText(key='senha', password_char='*')],
            [sg.Button('Entrar'), sg.Button('Sair'), sg.Button('Inscreva-se')]
        ]
        
        window = sg.Window('Login dos Professores', layout)
        while True:
            event, values = window.read()
            if event in (sg.WIN_CLOSED, 'Sair'):
                window.close()
                return
            
            if event == 'Inscreva-se':
                
                window.close()
                cad()
                return
            
            if event == 'Entrar':
                user = values['-us-']
                senha = values['senha']
                
                if user.isdigit():
                    sg.popup('O nome de usuário não pode ser numérico.')
                    continue
                
                if len(user) < 3:
                    if user == '':
                        sg.popup('As informações estão em branco.')
                    else:
                        sg.popup('O nome de usuário deve ter pelo menos 3 caracteres.')
                    continue
                
                user_found = False
                with open('dados_login.txt', 'r') as file:
                    for line in file:
                        file_user, file_senha = line.strip().split(',')
                        if file_user == user and file_senha == senha:
                            sg.popup('Login aceito!')
                            window.close
                            validar()
                            user_found = True
                            break
                
                if not user_found:
                    sg.popup('Esse usuário não existe ou a senha está incorreta. Por favor, verifique novamente ou faça a inscrição.')
                
                window.close()
                break
        
logar()