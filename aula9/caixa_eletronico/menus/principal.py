from getpass import getpass

from .menu import Menu
from .admin import menu_admin
from .cliente import menu_cliente
import usuarios

def menu_principal():
    menu = Menu(
        'Menu Principal',
        {
            'Fazer login': login
        }
    )

    while menu.executando():
        menu.cabecalho()
        menu.mostrar()
        entrada = menu.receber_entrada()

        if entrada is None:
            print("Digite uma opção válida\n")
            continue

        fn = menu.get_funcao_para_entrada(entrada)
        fn()

def login():
    username = input("Username: ")
    senha = getpass("Senha: ")

    u = usuarios.Usuario.login(username, senha)

    if u is None:
        print("Credenciais inválidas")

    elif isinstance(u, usuarios.Cliente):
        menu_cliente(u)

    elif isinstance(u, usuarios.Admin):
        menu_admin(u)

