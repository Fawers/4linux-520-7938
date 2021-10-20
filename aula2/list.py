nomes = [
    'Italo',
    'Vinicius',
    'Edson',
    'Dalton',
    'Paulo',
    'Nincao'
]

nomes_copia = nomes.copy()
nomes_copia.clear()

print('nomes_copia:', nomes_copia)
print('index of Edson:', nomes.index('Edson'))
nomes.insert(3, 'Fabio')
print('pós insert Fabio:', nomes)
print('lista popada:', nomes.pop())
print('pós pop:', nomes)
print('lista popada (index 2):', nomes.pop(2))
print('pós pop index 2:', nomes)
nomes.remove('Italo')
print('pós remove Italo:', nomes)
nomes.reverse()
print('pós reverse:', nomes)
nomes.sort()
print('pós sort:', nomes)
nomes.sort(reverse=True)
print('pós sort reversed:', nomes)

print("sobreviventes:")
for nome in nomes:
    print(nome)

nomes[0] = 'Vinicius Gibertoni'
nomes[1] += ' Roberto'
print(nomes)
