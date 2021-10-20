telefones = {
    'Fabricio': '123456789',
    'Luciano': '987654321',
    'Leonardo': '2345678'
}

print(telefones)

for nome in telefones:
    print(nome, telefones[nome])

print(telefones['Luciano'])
print(telefones.get('Diego'))
print(telefones.get('Fabricio'))

telefones['Veronica'] = '85265489'

for (nome, telefone) in telefones.items():
    print(telefone, 'é o número do(a)', nome)

print(telefones.setdefault('Gustavo', '74196358'))
print(telefones)
print(telefones.setdefault('Veronica', '74196358'))
telefones.update({
    'Marcus': '45678321',
    'Edilson': None
})

print(telefones)
