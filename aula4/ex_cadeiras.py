import time
import random


def contagem_regressiva(num):
    while num > 0:
        print(num, end='... ', flush=True)
        time.sleep(0.5)
        num -= 1

    print()


def criar_participantes(num_participantes):
    participantes = []

    for num in range(num_participantes):
        participantes.append(f"Participante-{num}")

    return participantes


def jogar(participantes):
    while len(participantes) > 1:
        print("dança da cadeira!")
        print("parando música em ", end='')
        contagem_regressiva(3)
        eliminado = random.randint(0, len(participantes)-1)
        print(f"{participantes.pop(eliminado)} foi eliminado!")
        print("Participantes:", participantes)
        time.sleep(1)

    return participantes.pop()


def main():
    num_p = int(input("Quantos participantes há? "))
    p = criar_participantes(num_p)
    print("Participantes:", p)
    vencedor = jogar(p)
    print("Vencedor:", vencedor)

print(__name__)  # <- execute o arquivo e também importando de outro arquivo
print(time.__name__)
print(random.__name__)

if __name__ == '__main__':
    main()
