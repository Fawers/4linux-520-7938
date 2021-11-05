from .menu import Menu

def menu_cliente(usuario_cliente):
    menu = Menu(
        'Área do Cliente',
        {
            'Consultar saldo': consultar_saldo,
            'Realizar saque': realizar_saque,
            'Realizar depósito': realizar_deposito,
            'Realizar transferência': realizar_transferencia,
            'Alterar senha': alterar_senha,
        },
        'Fazer logout'
    )

    while menu.executando():
        menu.cabecalho()
        menu.mostrar()
        entrada = menu.receber_entrada()

        if entrada is None:
            print("Digite uma opção válida\n")
            continue

        fn = menu.get_funcao_para_entrada(entrada)
        fn(usuario_cliente)

def consultar_saldo(usuario_cliente):
    saldo = usuario_cliente.get_saldo()
    print(f"O seu saldo é de R$ {saldo:.2f}")

def realizar_saque(usuario_cliente):
    quantia = float(input('Digite a quantia a sacar: '))
    novo_saldo = usuario_cliente.sacar(quantia)

    if novo_saldo is None:
        print("Não foi possível realizar o saque.")

    else:
        print(f"Saque realizado. Novo saldo: R$ {novo_saldo:.2f}")

def realizar_deposito(usuario_cliente):
    quantia = float(input('Digite a quantia a depositar: '))
    novo_saldo = usuario_cliente.depositar(quantia)

    if novo_saldo is None:
        print("Não foi possível realizar o depósito.")

    else:
        print(f"Depósito realizado. Novo saldo: R$ {novo_saldo:.2f}")

def realizar_transferencia(usuario_cliente):
    pass

def alterar_senha(usuario_cliente):
    pass
