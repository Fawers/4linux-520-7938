class Fruta:
    def __init__(self, nome, preco):
        self.__nome = nome
        self.__preco = preco

    def __repr__(self):  # representação textual
        return f"{self.__class__.__name__}({repr(self.__nome)}, R$ {self.__preco:.2f})"

    def __str__(self):
        return f"{self.__nome} (R$ {self.__preco:.2f})"

    def nome(self):
        return self.__nome

    def preco(self):
        return self.__preco


class Cesta:
    def __init__(self):
        self.__itens = {}

    def __repr__(self):
        return repr(self.__itens)

    def adicionar_fruta(self, fruta):
        self.__itens[fruta] = self.__itens.get(fruta, 0) + 1

    def esvaziar(self):
        self.__itens.clear()

    def calcular_total(self):
        total = 0

        for (item, quantidade) in self.__itens.items():
            total += item.preco() * quantidade

        return total


class Menu:
    def __init__(self, *opcoes):
        self.__opcoes = opcoes

    def mostrar_menu(self):
        for (i, opcao) in enumerate(self.__opcoes):
            print(f"{i} - {opcao}")
        print()

    def capturar_entrada(self, msg="Escolha uma opção: "):
        return int(input(msg))

    def get_item_para_entrada(self, entrada):
        return self.__opcoes[entrada]

quitanda = [
    Fruta("Banana", 3.50),
    Fruta("Melancia", 7.50),
    Fruta("Morango", 5.00)
]

def add_frutas(cesta):
    menu_frutas = Menu(*quitanda, 'Sair')

    while True:
        menu_frutas.mostrar_menu()
        fruta = menu_frutas.get_item_para_entrada(
            menu_frutas.capturar_entrada())

        if fruta == 'Sair':
            break

        else:
            cesta.adicionar_fruta(fruta)

def main():
    menu_principal = Menu('Ver cesta', 'Adicionar frutas', 'Checkout', 'Sair')
    cesta = Cesta()

    while True:
        menu_principal.mostrar_menu()
        entrada = menu_principal.capturar_entrada()
        entrada = menu_principal.get_item_para_entrada(entrada)

        if entrada == 'Sair':
            break

        elif entrada == 'Ver cesta':
            print(cesta)

        elif entrada == 'Adicionar frutas':
            add_frutas(cesta)

        elif entrada == 'Checkout':
            print(cesta)
            print(f"R$ {cesta.calcular_total():.2f}")

if __name__ == '__main__':
    main()
