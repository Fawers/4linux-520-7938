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

def main():
    nome_arquivo = 'ex_2.json'

    with open(nome_arquivo) as a:
        regs = carregar(a)

    reg = requisitar_dados()

    regs['registros'].append(reg)

    with open(nome_arquivo, 'w') as a:
        salvar(regs, a)

if __name__ == '__main__':
    main()
