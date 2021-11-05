class Menu:
    def __init__(self, titulo, opcoes, opcao_saida='Sair'):
        self.__titulo = titulo.strip()
        self.__opcoes = opcoes
        self.__executanto = True

        self.__opcoes[opcao_saida] = self.finalizar

    def cabecalho(self):
        tam_titulo = len(self.__titulo)
        print('=' * tam_titulo)
        print(self.__titulo)
        print('=' * tam_titulo)
        print()

    def mostrar(self):
        for (opcao, descricao) in enumerate(self.__opcoes.keys()):
            print(f"{opcao} - {descricao}")

        print()

    def receber_entrada(self, msg='Digite uma opção: '):
        try:
            entrada = int(input(msg))

            if entrada < 0:
                return None

            return list(self.__opcoes.keys())[entrada]

        except (ValueError, IndexError):
            return None

    def get_funcao_para_entrada(self, entrada):
        return self.__opcoes[entrada]

    def executando(self):
        return self.__executanto

    def finalizar(self, *_):
        self.__executanto = False
