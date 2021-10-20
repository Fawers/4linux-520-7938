dados = ('Fabricio', 29, '4Linux')

print(dados[0])
print(dados[1])
print(dados[2])

for dado in dados:
    print(f"dado é {dado}")

(nome, idade, trabalho) = dados
print(f"nome:     {nome}")
print(f"idade:    {idade}")
print(f"trabalho: {trabalho}")

(cidade, estado, pais) = ('Ubatuba', 'São Paulo', 'Brasil')
print(cidade, estado, pais)

print(dados.count(29))
print(dados.index('4Linux'))

turma = (520, 7938, ['Luciano'])
turma[2].append('Saulo')
print(turma)
# turma[0] = 123456789  # <-- erro!
