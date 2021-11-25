from .menu import Menu
from db import usuarios
from usuarios import Cliente

def menu_admin(usuario_admin):
    menu = Menu(
        'Menu Administrativo',
        {
            'Cadastrar novo cliente': cadastrar_cliente,
            'Desbloquear cliente': desbloquear_cliente
        },
        opcao_saida='Fazer logout'
    )

    while menu.executando():
        menu.cabecalho()
        menu.mostrar()
        entrada = menu.receber_entrada()

        if entrada is None:
            print("Digite uma opção válida\n")
            continue

        fn = menu.get_funcao_para_entrada(entrada)
        fn(usuario_admin)

def cadastrar_cliente(usuario_admin):
    username = input("Digite o username da nova conta: ")
    criado = usuario_admin.cadastrar_cliente(username)

    if criado:
        print(f"Usuário `{username}` criado com sucesso.")

    else:
        print("Não foi possível cadastrar o novo usuário.")

def desbloquear_cliente(usuario_admin):
    username = input("Digite o username da conta bloqueada: ")
    dados = usuarios.buscar(username)

    if dados is None:
        print("Conta não encontrada.")

    elif usuario_admin.desbloquear_cliente(Cliente(**dados)):
        print("Usuário desbloqueado com sucesso.")

    else:
        print(f"Ocorreu um problema ao desbloquear o usuário `{username}`.")
