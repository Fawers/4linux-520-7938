pilha = []

def empilhar(item):
    pilha.append(item)

def desempilhar():
    return pilha.pop()


empilhar(1)
print(pilha)
empilhar(2)
print(pilha)
empilhar(3)
print(pilha)
empilhar(4)
print(pilha)

print(desempilhar())
print(desempilhar())
print(desempilhar())
print(desempilhar())
print(pilha)
