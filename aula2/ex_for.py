# Dada uma string fornecida pelo usuário (input),
# printar na tela cada caractere seguido de uma informação:
# se o caractere é uma letra maiúscula, minúscula, número, ou
# alguma outra coisa.

# Dica: colocar ponto após string e estudar operações possíveis

string = input("> ")

for c in string:
    if c.isupper():
        print(f"caractere {c} é maiúsculo")

    elif c.islower():
        print(f"caractere {c} é minúsculo")

    elif c.isnumeric():
        print(f"caractere {c} é um número")

    else:
        print(f"caractere {c} é alguma outra coisa")


