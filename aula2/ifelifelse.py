habilitado = input("Você é habilitado? ").lower().strip()
# habilitado = habilitado.lower()

if habilitado.startswith('s'):
    print("Você pode dirigir!")

elif habilitado.startswith('n'):
    print("Você não deve dirigir...")

elif habilitado.find('s') != -1:
    print("Acho que vc pode dirigir...")

else:
    print("Não entendi.")
