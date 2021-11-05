from .menu import Menu

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
    usuario_admin.cadastrar_cliente('cliente')

def desbloquear_cliente(usuario_admin):
    print('desbloquear_cliente')
