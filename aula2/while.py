valor = 11

while valor > -1:
    valor -= 1
    if valor % 2 != 0:
        continue  # abaixo daqui não me interessa; RECOMEÇAR loop

    # if valor == 0:
    #     break

    print("Valor:", valor)

else:
    print("Fim do loop!")

print("Fora do loop! Ufa!")
