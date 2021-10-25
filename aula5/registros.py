from pprint import pprint


def ler_registros_dict(arquivo):
    linhas = []
    cabecalho = arquivo.readline().strip().split("\t")

    for linha in arquivo:
        linha = linha.strip().split("\t")
        pares = zip(cabecalho, linha)
        # registro = dict(pares)
        # linhas.append(registro)
        linhas.append(dict(pares))

    return linhas

def ler_registros_lista(arquivo):
    linhas = []
    cabecalho = arquivo.readline().strip().split("\t")

    linhas.append(cabecalho)

    for linha in arquivo:
        linhas.append(linha.strip().split('\t'))

    return linhas

def main():
    with open('registros.txt') as a:
        # regs = ler_registros_lista(a)
        regs = ler_registros_dict(a)

    pprint(regs)


if __name__ == '__main__':
    main()
