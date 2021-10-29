# Criar a estrutura de cursos da 4Linux.
# Classes: Curso, Turma

# Curso:
# - id (int)
# - nome
# - __str__() ou __repr__() => "520 Python Fundamentals"

class Curso:
    id = 520
    nome = "Python Fundamentals"

    def __init__(self, id, nome):
        self.__id = id
        self.__nome = nome
        self.__turmas = []

    def __repr__(self):
        # return str(self.__id) + ' ' + self.__nome
        # return f"{self.__id} {self.__nome}"
        return f"Curso({self.__id}, {self.__nome})"

    def criar_turma(self, id, alunos):
        t = Turma(id, self, alunos)
        self.__turmas.append(t)
        return t

    def imprimir_turmas(self):
        for turma in self.__turmas:
            print(turma)

# Turma:
# - id (int)
# - curso
# - alunos ([string])
# - __str__() ou __repr__() => "520 Python Fundamentals 7938"
# - chamada() => imprimir linha a linha o nome dos alunos

class Turma:
    def __init__(self, id, curso, alunos):
        self.id = id
        self.__curso = curso
        self.__alunos = alunos

    def __repr__(self):
        # return f"{self.__curso} {self.id}"
        return f"Turma({self.id})"

    def chamada(self):
        for aluno in self.__alunos:
            print(aluno)


def main():
    c = Curso(520, 'Python Fundamentals')
    cursos = [
        c,
        Curso(521, 'Python for SysAdmins'),
    ]
    print(cursos)

    # t = Turma(7938, c, ['Fulano', 'Ciclano', 'Beltrano'])
    # linha acima e abaixo são similares;
    # linha comentada NÃO salva na lista de turmas do curso
    t = c.criar_turma(7938, ['Fulano', 'Ciclano', 'Beltrano'])
    cursos[1].criar_turma(7939, ['Fulano', 'Beltrano'])
    print(t)
    # print(t.curso, t.curso is c)
    t.chamada()
    c.imprimir_turmas()
    cursos[1].imprimir_turmas()

if __name__ == '__main__':
    main()
