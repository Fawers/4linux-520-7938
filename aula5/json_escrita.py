import json

import registros


def main():
    with open('registros.txt') as txt:
        regs = registros.ler_registros_dict(txt)

    dados = {'registros': regs}
    print(dados)

    with open('registros.json', 'w') as json_f:
        json.dump(dados, json_f, indent='  ')


if __name__ == '__main__':
    main()
