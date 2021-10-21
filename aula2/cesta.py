cesta = {
    'banana': 2,
    'melancia': 5,
    'morango': 10
}

cesta.items()

cesta_items = [
    ('banana', 2),
    ('melancia', 5),
    ('morango', 10),
]

ci = cesta.items()
cil = list(ci)

print(ci, type(ci))
print(cil, type(cil))

print(cil == cesta_items)
