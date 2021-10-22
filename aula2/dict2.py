curso = 'Python Fundamentals'
turma = 7938
turmas = [
    {}
]
x, y = 13, 17

ecosistema = {
    "curso": "Python Fundamentals",
    "turmas": {
        7938: {
            "alunos": ["Vinicius"]
        }
    }
}

print(curso, turma)
print(ecosistema["curso"], ecosistema["turmas"])

adicao = lambda x, y: x + y
adicao(x, y)

def subtracao(x, y):
    return x - y

operacoes = {
    "adicao": lambda x, y: x + y,
    "subtracao": subtracao
}

operacoes["adicao"](x, y)

def div(x, y):
    x / y

fns = [
    lambda x, y: x * y,
    div
]
