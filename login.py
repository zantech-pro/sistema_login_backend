#Imports
import json
import os
import time
from os.path import exists
import getpass
import hashlib

#Tela de Login
def login():
    print('\n')
    print('*' * 50)
    print(' Area de Autenticação '.center(50,'#'))
    print('*' * 50)
    print('Opções:')
    print('1 - Efetuar Login')
    print('2 - Esqueceu Senha?')
    print('3 - Cadastra-se')
    print('4 - Sair')
    print('\n')

    try:
        option = int(input('Digite a opção desejada >>> '))

        if option == 1:
            os.system('cls')
            start_login()

        elif option == 2:
            os.system('cls')
            recuperar_senha()

        elif option == 3:
            os.system('cls')
            cadastrar_usuario()

        elif option == 4:
            os.system('cls')
            print('Saindo do sistema...')
            quit()
        else:
            print('Opção invalida. Tente novamente...')
            time.sleep(1.3)
            os.system('cls')
            login()

    except ValueError as error:
        print(f'Entrada de dados invalida!, reiniciaremos o sistema.... mensagem de erro {error}')
        time.sleep(1.3)
        os.system('cls')
        login()

def start_login():
    print('\n')
    print('*' * 50)
    print(' Efetuar Login '.center(50, '#'))
    print('*' * 50)
    user = input('Digite Nome de usuario >>> ')
    senha = getpass.getpass('Digite senha >>> ')

    if check(user, hashlib.sha256(senha.encode('utf-8')).hexdigest()):
        print("Login com sucesso! vamos te redirecionando...")
        time.sleep(1.3)
        os.system('cls')
        tela_de_login()
    else:
        print('\nLogin/Senha incorretos. Tente novamente...')
        time.sleep(1.3)
        os.system('cls')
        login()
def recuperar_senha():
    print('*' * 50)
    print(' Esqueceu sua senha? Vamos te ajudar a recuperar... '.center(50, '#'))
    print('*' * 50)
    print('Nos informe:')

    try:
        date_birth = input('Digite sua data de nascimento (Formato DD/MM/AAAA) >>> ')
        time.strptime(date_birth, '%d/%m/%Y') #força erro caso formato da date_birth esteja no formato errado
    except Exception as error:
        print(f'Data invalida gerando erro, formato correto é DIA/Mês/Ano exemplo: 25/08/2025')
        print(f'Recarregando o menu de recuperação de senha...')
        time.sleep(1.5)
        os.system('cls')
        recuperar_senha()

    email = input('Digite o email >>> ')
    if '@' in email:
        if '.' in email.split('@')[1]:
            pass
        else:
            print(f'E-mail invalido...')
            print(f'Recarregando o menu de recuperação de senha...')
            time.sleep(1.5)
            os.system('cls')
            recuperar_senha()
    else:
        print(f'E-mail invalido...')
        print(f'Recarregando o menu de recuperação de senha...')
        time.sleep(1.5)
        os.system('cls')
        recuperar_senha()

    palavra_secreta = input('Digite sua palavra secreta >>> ')

    if check_recupera(date_birth, email,  palavra_secreta):
        nova_senha = getpass.getpass('\nDigite nova senha >>> ')
        nova_senha_r = getpass.getpass('\nConfirmar a senha >>> ')

        if nova_senha == nova_senha_r:
            if alterar_credenciais(email, palavra_secreta, hashlib.sha256(nova_senha.encode('utf-8')).hexdigest()):
                print('Redefinido senha com sucesso!')
                print('Redirecionado para tela de login...')
                time.sleep(1.5)
                os.system('cls')
                login()
            else:
                print('Erro ao tentar altera senha. Tente novamente...')
                time.sleep(1.5)
                os.system('cls')
                recuperar_senha()
        else:
            print('Senhas não são iguais. Tente novamente...')
            print('Redirecionado para tela de login...')
            time.sleep(1.5)
            os.system('cls')
            recuperar_senha()
    else:
        print('Dados não incosistentes...')
        print('Redirecionado para tela de login...')
        time.sleep(1.5)
        os.system('cls')
        login()

def alterar_credenciais(email, palavra_secreta, nova_senha):
    if exists('base_dados.json'):
        with open('base_dados.json', 'r', encoding='utf-8') as usuarios:
            dados_json = json.load(usuarios)

        if 'usuarios' in dados_json:
            return False
        else:
            conjunto_registro = []
            for item in dados_json:
                if item['email'] == email and item['palavra_secreta'] == palavra_secreta:
                    item['password'] = nova_senha
                    conjunto_registro.append(item)
                else:
                    conjunto_registro.append(item)
            cont = 0
            with open('base_dados.json', 'w', encoding='utf-8') as usuarios:
                dados_json_new = json.dumps(conjunto_registro, indent=4, ensure_ascii=False)
                usuarios.write(dados_json_new)
                cont += 1

            if cont > 0:
                return True
            else:
                return False
    else:
        with open('base_dados.json', 'w', encoding='utf-8') as file:
            estrutura_user = {'usuarios': 'vazio', 'msg': 'vazio'}
            json.dump(estrutura_user, file, ensure_ascii=False, indent=4)

        alterar_credenciais(email, palavra_secreta)

def check_recupera(date_birth, email,  palavra_secreta):
    if exists('base_dados.json'):
        with open('base_dados.json', 'r', encoding='utf-8') as usuarios:
            dados_json = json.load(usuarios)

        if 'usuarios' in dados_json:
            return False
        else:
            for item in dados_json:
                if item['date_birth'] == date_birth and item['email'] == email and item['palavra_secreta'] == palavra_secreta:
                    return True
            else:
                return False
    else:
        with open('base_dados.json', 'w', encoding='utf-8') as file:
            estrutura_user = {'usuarios': 'vazio', 'msg': 'vazio'}
            json.dump(estrutura_user, file, ensure_ascii=False, indent=4)

        check_recupera(date_birth, email, palavra_secreta)



def check(user, senha):

    if exists('base_dados.json'):
        with open('base_dados.json', 'r', encoding='utf-8') as usuarios:
            dados_json = json.load(usuarios)

        if 'usuarios' in dados_json:
            return False
        else:
            if str(type(dados_json)) == "<class 'dict'>":
                dados_json = [dados_json]

            for item in dados_json:    
                if item['user'] == user and item['password'] == senha:
                    return True
            
            return False
    else:
         with open('base_dados.json', 'w', encoding='utf-8') as file:
             estrutura_user = {'usuarios': 'vazio', 'msg': 'vazio'}
             json.dump(estrutura_user, file, ensure_ascii=False, indent=4)

         check(user, senha)

def tela_de_login():
    print('\n')
    print('*' * 50)
    print('Bem-vindo ao login do sistema...')
    print('*' * 50)
    print('\n')
    opt = int(input('Digite 1 para deslogar >>> '))
    if opt == 1:
        print('Deslogando...')
        time.sleep(1.3)
        os.system('cls')
        login()

def cadastrar_usuario():
    print('\n')
    print('*' * 50)
    print(' Formulario de Cadastro de novo Usuario '.center(50,'#'))
    print('*' * 50)

    nome_full = input('- Nome Completo (min. 11 caracteres): ')
    if len(nome_full) > 10:
        if len(nome_full.split(' ')) > 1:
            pass
        else:
            print(f'Tamanho do nome não aceito, min. 11 caracteres com sobrenome.. Favor refazer o formulario...')
            time.sleep(1.5)
            os.system('cls')
            login()
    else:
        print(f'Tamanho do nome não aceito, min. 11 caracteres com sobrenome.. Favor refazer o formulario...')
        time.sleep(1.5)
        os.system('cls')
        login()

    try:
        date_birth = input('- Data de Nascimento (Formato: DD/MM/AAAA): ')
        time.strptime(date_birth, '%d/%m/%Y') #força erro caso formato da date_birth esteja no formato errado
    except Exception as error:
        print(f'Data invalida gerando erro, formato correto é Dia/Mês/Ano exemplo: 25/08/2025')
        time.sleep(1.5)
        os.system('cls')
        login()


    email = input('- Email: ')
    if '@' in email:
        if '.' in email.split('@')[1]:
            pass
        else:
            print(f'E-mail invalido... Favor refazer o formulario...')
            time.sleep(1.5)
            os.system('cls')
            login()
    else:
        print(f'E-mail invalido... Favor refazer o formulario...')
        time.sleep(1.5)
        os.system('cls')
        login()

    user = input('- Usuario (Min. 10 caracteres): ')
    if len(user) > 9:
        pass
    else:
        print(f'Tamanho do nome de usuario não aceito, min. 10 caracteres... Favor refazer o formulario...')
        time.sleep(1.5)
        os.system('cls')
        login()

    password = getpass.getpass("- Senha (Min. 8 caracters): ")
    password_repeat = getpass.getpass("- Repita a Senha: ")

    if len(password) > 7:
        if password == password_repeat:
            pass
        else:
            print(f'Senha e Repetir senha são diferentes... Favor refazer o formulario...')
            time.sleep(1.5)
            os.system('cls')
            login()
    else:
        print(f'Tamanho da senha não aceito, min. 8 caracteres... Favor refazer o formulario...')
        time.sleep(1.5)
        os.system('cls')
        login()

    palavra_secreta = input('- Palavra secreta(Frase secreta pode ser qualquer coisa min. 12 caracteres): \nCidade que morou ou animal de estimação etc...) >>> ')

    if len(palavra_secreta) > 11:
        pass
    else:
        print(f'Minimo da palavra secreta e de 12 caracteres... Favor refazer o formulario...')
        time.sleep(1.5)
        os.system('cls')
        login()

    print('\n')
    option = input('Pressione <<Enter>> para salvar ou digite 1 para sair')

    if option == '':

        dados = {"user": user,
                    "password": hashlib.sha256(password.encode('utf-8')).hexdigest(),
                    "email": email,
                    "palavra_secreta": palavra_secreta,
                    "nome_full": nome_full,
                "date_birth": date_birth}

        base_dados('salvar', **dados)
        os.system('cls')
    elif option == '1':
        print('Saindo, retornando para menu...')
        time.sleep(1.3)
        os.system('cls')
        login()
    else:
        print('Opção invalida...')
        time.sleep(1.3)
        os.system('cls')
        login()



def base_dados(comando, **options):
    if exists('base_dados.json'):

        if comando == 'salvar':
            novo_usuario = options
            dados_jason = ''
            with open('base_dados.json', 'r', encoding='utf-8') as file:
                dados_jason = json.load(file)

            if 'usuarios' in dados_jason:
                id = 1
                novo_usuario['id'] = id
                with open('base_dados.json', 'w', encoding='utf-8') as file:
                    dados_json_new = json.dumps(novo_usuario, indent=4, ensure_ascii=False)
                    file.write(dados_json_new)
            else:
                #Algoritimo do ID novo
                lista_id = []
                tipo = 0
                if str(type(dados_jason)) == "<class 'dict'>":
                    for item in [dados_jason]:

                        lista_id.append(item['id'])
                    lista_id.sort()
                    id_novo = int(lista_id[-1]) + 1
                    tipo = 1

                elif str(type(dados_jason)) == "<class 'list'>":
                    for item in dados_jason:
                        lista_id.append(item['id'])
                    lista_id.sort()
                    id_novo = int(lista_id[-1]) + 1
                    tipo = 2
                else:
                    print('Erro na leitura de dados jason...')

                # Verificar se usuario e email existe
                check = 0

                if tipo == 1:
                    dados_jason = [dados_jason]
                elif tipo == 2:
                    pass

                for registro in dados_jason:
                    if novo_usuario['user'] == registro['user'] and novo_usuario['email'] == registro['email']:
                        check+=1
                    if novo_usuario['email'] == registro['email']:
                        check+=1

                if check > 0:
                    print('Usuario já cadastrado!!!')
                else:
                    novo_usuario['id'] = id_novo
                    nova_lista = []
                    for item in dados_jason:
                        nova_lista.append(item)
                    nova_lista.append(novo_usuario)

                    with open('base_dados.json', 'w', encoding='utf-8') as file:
                        dados_json_new = json.dumps(nova_lista, indent=4, ensure_ascii=False)
                        file.write(dados_json_new)
                        print("Registro salvo com sucesso!")

            print("Retornando ao menu...")
            time.sleep(1.3)
            os.system('cls')
            login()

    else:
        with open('base_dados.json', 'w', encoding='utf-8') as file:
            estrutura_user = {'usuarios': 'vazio', 'msg': 'vazio'}
            json.dump(estrutura_user, file, ensure_ascii=False, indent=4)

        print("Carregando a base de dados...")
        time.sleep(1.3)
        os.system('cls')
        opt = options
        base_dados(comando, **opt)

#Started system of login
login()
