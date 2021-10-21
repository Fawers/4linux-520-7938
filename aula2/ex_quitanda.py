# 2) Escreva um script em python que represente uma quitanda. O seu programa deverá
# apresentar as opções de frutas, e a cada vez que você escolher a fruta desejada, a fruta
# deverá ser adicionada a uma cesta de compras.

cesta = {}

# Menu principal:
# 1 Quitanda:
# 2 1: Ver cesta
# 3 2: Adicionar frutas
# 4 3: Sair
# 5
# 6 Digite a opção desejada:
# 1 Menu de frutas:
# 2
# 3 Escolha fruta desejada:
# 4 1 - Banana
# 5 2 - Melancia
# 6 3 - Morango
# 7
# 8 Digite à opção desejada: 2
# 9 Melancia adicionada com sucesso!
# Os menus 1 e 2 deverão retornar ao menu principal após executar as suas tarefas.
# Você deverá validar as opções digitadas pelo usuário (caso ele digitar algo errado, a mensagem
# Digite uma opção inválida)

quitanda = {
    'Banana': 3.50,
    'Melancia': 7.50,
    'Morango': 5.00
}

while True:
    print()
    print("-" * 20)
    print("Bem-vindo à quitanda Pytheira!")
    print("1: Ver cesta")
    print("2: Adicionar frutas")
    print("3: Checkout")
    print("4: Sair")

    entrada = int(input('Digite a opção desejada: '))

    if entrada == 4:
        print("Até logo!")
        break

    elif entrada == 1:
        print("Cesta de frutas:", cesta)

    elif entrada == 2:
        print("=" * 20)
        quitanda_ks = list(quitanda.keys())
        while True:
            for (i, fruta) in enumerate(quitanda_ks):
                print(f"{i}: {fruta}")
            print('-1: Sair')

            entrada = int(input("Digite a fruta/opção desejada: "))

            if entrada == -1:
                break

            elif 0 <= entrada < len(quitanda_ks):
                fruta = quitanda_ks[entrada]
                cesta[fruta] = cesta.get(fruta, 0) + 1

            else:
                print("Digite uma opção válida.")

    elif entrada == 3:
        print("Cesta:", cesta)

        total = 0
        for (fruta, quantidade) in cesta.items():
            total += quantidade * quitanda[fruta]

        print(f"Total: R$ {total}")

    else:
        print("Digite uma opção válida.")



# 54 2. CONTROLES DE FLUXO E ESTRUTURAS DE REPETIÇÃO
# O programa deverá ser encerrado apenas se o usuário digitar a opção 3.
# 3) Aproveitando o exercício anterior, incremente a sua quitanda para consolidar o valor
# total de sua cesta de compras. Deverá ser adicionado ao seu menu inicial a opção
# checkout e esta deverá listar os produtos de sua cesta bem como o valor total:
# 1 Menu:
# 2 1: Ver cesta
# 3 2: Adicionar Frutas
# 4 3: Checkout
# 5 4: Sair
# 6
# 7 Digite a opção desejada:
# A saída do checkout deverá ser da seguinte maneira:
# 1 Total de compras: 15,00
# 2 Cesta de compras: Banana, Morango, Melancia
# Considere os seguintes preços:
# Banana: 3.50 Melancia: 7.50 Morango: 5.00
# Dica: Você pode armazenar os dados de frutas e seus respectivos preços em um dicionário.
