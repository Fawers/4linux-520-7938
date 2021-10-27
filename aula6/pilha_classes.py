class Pilha:
    def __init__(self, limite=10):
        self.__pilha = []
        self.__limite = limite

    def empilhar(self, item):
        if not self.cheia():
            self.__pilha.append(item)
            return True

        return False

    def desempilhar(self):
        if not self.vazia():
            return self.__pilha.pop()

        return None

    def topo(self):
        if not self.vazia():
            return self.__pilha[-1]

        return None

    def vazia(self):
        return len(self.__pilha) == 0

    def cheia(self):
        return len(self.__pilha) == self.__limite


def main():
    p = Pilha(5)
    p.empilhar(1)
    p.empilhar(2)
    p.empilhar(3)
    p.empilhar(4)
    print(p.cheia())

    p.empilhar(5)
    print(p.cheia())

    print(p.topo())
    print(p.desempilhar())
    print(p.topo())

    while not p.vazia():
        print(p.desempilhar())

    print(p.topo())
    print(p.vazia())

    # p2 = Pilha(5)
    # p2.empilhar('string')
    # print(p2.get_pilha())


if __name__ == '__main__':
    main()

# pilha_dict = {"limite": 5, "p": []}
# pilha_dict['limite'] = 500
# pilha_dict["p"].clear()
# pilha_obj = Pilha(5)
# pilha_obj.__pilha.clear()
# pilha_obj.__limite = 500
