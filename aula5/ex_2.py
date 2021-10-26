# 2) Escreva um programa em python que realize um cadastro. Deverão ser coletadas as
# seguintes informações:
# • CPF
# • Nome
# • Idade
# • Endereço
# 3) Implemente uma função de consulta no programa do exercício 2.
# 4) Implemente uma função de exclusão no programa do exercício 2.

import json

def requisitar_dados():
    d = {}

    for campo in ('cpf', 'nome', 'idade', 'endereço'):
        d[campo] = input(f'Digite {campo.upper()}: ').strip()

    return d

def salvar(dados, arquivo):
    json.dump(dados, arquivo, indent=4)

def carregar(arquivo):
    return json.load(arquivo)

def adicionar(regs):
    regs['registros'].append(requisitar_dados())
    return True

def consultar(regs):
    nome = input("Digite um nome para buscar: ").strip()

    for reg in regs["registros"]:
        if reg['nome'] == nome:
            print(reg)
            break

    return False

def remover(regs):
    nome = input("Digite um nome para remover: ").strip()

    for reg in regs["registros"]:
        if reg['nome'] == nome:
            regs['registros'].remove(reg)
            return True

    return False

def main():
    nome_arquivo = 'ex_2.json'

    with open(nome_arquivo) as a:
        regs = carregar(a)

    opcoes = {
        '1': ('Adicionar registro', adicionar),
        '2': ('Consultar', consultar),
        '3': ('Remover registro', remover),
        '-1': ('Finalizar', lambda: None)
    }

    while True:
        for (opcao, (descricao, _)) in opcoes.items():
            print(f"{opcao} - {descricao}")
        entrada = input("Escolha uma opção: ")

        if entrada == '-1':
            break

        # O código comentado abaixo substitui os próximos elif
        # elif entrada in opcoes:
        #     (_, fn) = opcoes[entrada]

        #     if fn(regs):
        #         with open(nome_arquivo, 'w') as a:
        #             salvar(regs, a)

        elif entrada == '1':
            adicionar(regs)  # precisa salvar de qlq jeito
            with open(nome_arquivo, 'w') as a:
                salvar(regs, a)

        elif entrada == '2':
            consultar(regs)

        elif entrada == '3':
            deve_salvar = remover(regs)
            if deve_salvar:  # descobre primeiro se precisa salvar
                with open(nome_arquivo, 'w') as a:
                    salvar(regs, a)

        else:
            print("Digite uma opção válida")

if __name__ == '__main__':
    main()
