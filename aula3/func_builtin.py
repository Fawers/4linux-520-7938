print(1, 2, 4, 8, 16, 32, end='.\n', sep=', ')

# print(input("digite: "))

frutas = 'Banana Melancia Morango Uva Caju Pera Maçã'.split()
print(frutas)

for (index, fruta) in enumerate(start=0, iterable=frutas):
    print(index, fruta, sep=': ')
