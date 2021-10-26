# 1) Escreva um programa em python que conte as vogais que a música ‘Faroeste Caboclo’
# tem em sua letra. Armazena a letra da música em um arquivo do tipo txt.
# Dica: Não se esqueça de considerar as letras maiúsculas, minúsculas e com acentuação.

def contar_vogais(letra):
    vogais = 0

    for caractere in letra.lower():
        # for v in ('a', 'e', 'i', 'o', 'u'):
        #     if caractere == v:
        #         vogais += 1
        #         break

        if caractere in 'aeiou':
            vogais += 1

    return vogais

def main():
    with open('hellraiser.txt') as a:
        letra_de_musica = a.read()

    print("Vogais:", contar_vogais(letra_de_musica))


if __name__ == '__main__':
    main()
