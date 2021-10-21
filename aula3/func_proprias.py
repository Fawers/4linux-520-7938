def somar(*valores):
    soma = 0

    for num in valores:
        soma += num

    return soma


def montar_nome(*nomes, **opcoes):
    print(opcoes)
    sep = opcoes.get('sep', ' ')
    return sep.join(nomes)
