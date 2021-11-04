import sqlite3
import db


class Setor:
    def __init__(self, nome, andar, num_colaboradores, id=None):
        self.id = id
        self.nome = nome
        self.andar = andar
        self.colaboradores = num_colaboradores

    def __str__(self):
        return f"{self.nome}[{self.andar}] : {self.colaboradores} colaboradores"

    def salvar(self):
        conn = db.sqlite3.connect("db.sqlite3")

        if self.id is not None:  # id já existe
            db.atualizar_dados(
                conn,
                [
                    f"'nome' = {repr(self.nome)}",
                    f"'andar' = {repr(self.andar)}",
                    f"'colaboradores' = {repr(self.colaboradores)}",
                ],
                self.id)

        else:  # id não existe
            self.id = db.inserir_dados(conn, [(self.nome, self.andar, self.colaboradores)])

        conn.close()

    def remover(self):
        conn = db.sqlite3.connect("db.sqlite3")
        db.remover_dados(conn, self.id)
        conn.close()

    @classmethod
    def carregar(cls, id):
        conn = db.sqlite3.connect("db.sqlite3")
        dados = db.selecionar_dados(conn, ('nome', 'andar', 'colaboradores'), id)
        conn.close()

        if dados is None:
            return None

        return Setor(*dados)

def ver_setor():
    id_setor = int(input('Digite o id do setor: '))

    s = Setor.carregar(id_setor)

    if s is None:
        print("Nenhum setor encontrado")

    else:
        print(s)

def adicionar_setor():
    nome = input('Digite o nome do novo setor: ')
    andar = int(input('Digite o andar do novo setor: '))
    colaboradores = int(input('Digite o número de colaboradores do novo setor: '))

    s = Setor(nome, andar, colaboradores)
    s.salvar()
    print(s)
    print(s.id)

def modificar_setor():
    id_setor = int(input('Digite o id do setor: '))
    s = Setor.carregar(id_setor)

    if s is None:
        print("Setor não encontrado\n")
        return

    print(s)
    s.nome = input('Digite o novo nome do setor: ')
    s.andar = int(input('Digite o novo andar do setor: '))
    s.colaboradores = int(input('Digite o novo número de colaboradores do setor: '))

    s.salvar()
    print(s)

def remover_setor():
    id_setor = int(input('Digite o id do setor: '))
    s = Setor.carregar(id_setor)

    if s is None:
        print("Setor não encontrado\n")
        return

    s.remover()

def listar_setores():
    conn = sqlite3.connect("db.sqlite3")
    setores_raw = db.selecionar_todos(conn, ('nome', 'andar', 'colaboradores'))

    for s in setores_raw:
        print(Setor(*s))

    conn.close()

def main():
    while True:
        menu = ['Ver setor', 'Adicionar setor', 'Modificar setor',
                'Remover setor', 'Listar setores', 'Sair']

        for (opcao, descricao) in enumerate(menu):
            print(f"{opcao} - {descricao}")

        try:
            entrada = int(input('Selecione uma opção: '))
            escolha = menu[entrada]

        except:
            print("Digite uma opção válida\n")
            continue

        if escolha == 'Sair':
            break

        elif escolha == 'Ver setor':
            ver_setor()

        elif escolha == 'Adicionar setor':
            adicionar_setor()

        elif escolha == 'Modificar setor':
            modificar_setor()

        elif escolha == 'Remover setor':
            remover_setor()

        elif escolha == 'Listar setores':
            listar_setores()

if __name__ == '__main__':
    main()
