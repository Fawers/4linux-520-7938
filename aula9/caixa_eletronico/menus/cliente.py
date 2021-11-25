from getpass import getpass

from .menu import Menu
from usuarios import Cliente
from db import usuarios


def menu_cliente(usuario_cliente: Cliente):
    if usuario_cliente.primeiro_acesso():
        usuario_cliente.resetar_primeiro_acesso()
        alterar_senha(usuario_cliente)

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


def _get_quantia(input_msg='Digite a quantia: ',
                 err_msg='Digite uma quantia válida.'):
    while True:
        try:
            return float(input(input_msg))

        except ValueError:
            print(err_msg)


def realizar_saque(usuario_cliente):
    quantia = _get_quantia('Digite a quantia a sacar: ')
    novo_saldo = usuario_cliente.sacar(quantia)

    if novo_saldo is None:
        print("Não foi possível realizar o saque.")

    else:
        usuario_cliente.salvar()
        print(f"Saque realizado. Novo saldo: R$ {novo_saldo:.2f}")


def realizar_deposito(usuario_cliente):
    quantia = _get_quantia('Digite a quantia a depositar: ')
    novo_saldo = usuario_cliente.depositar(quantia)

    if novo_saldo is None:
        print("Não foi possível realizar o depósito.")

    else:
        usuario_cliente.salvar()
        print(f"Depósito realizado. Novo saldo: R$ {novo_saldo:.2f}")


def realizar_transferencia(usuario_cliente):
    quantia = _get_quantia()
    username_destino = input('Digite o nome de usuário destinatário: ')
    dados_dest = usuarios.buscar(username_destino)

    if dados_dest is None:
        print(f"Usuário `{username_destino}` não encontrado.")

    else:
        destinatario = Cliente(**dados_dest)
        novos_saldos = usuario_cliente.transferir(destinatario, quantia)

        if novos_saldos is None:
            print("Não foi possível concluir a transferência.")
            return

        usuario_cliente.salvar()
        destinatario.salvar()
        (nsr, nsd) = novos_saldos

        print("Transferência realizada.")
        print(f"Novo saldo do remetente: R$ {nsr:.2f}")
        print(f"Novo saldo do destinatário: R$ {nsd:.2f}")


def alterar_senha(usuario_cliente):
    while True:
        senha_a = getpass('Digite uma nova senha: ')
        senha_b = getpass('Digite novamente a nova senha: ')

        if senha_a == senha_b:
            break

        print('As senhas não podem ser diferentes.')

    usuario_cliente.alterar_senha(senha_a)
    usuario_cliente.salvar()
