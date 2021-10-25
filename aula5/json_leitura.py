import json


def main():
    with open('registros.json') as json_file:
        # conteudo_json = json_file.read()
        # regs = json.loads(conteudo_json)
        regs = json.load(json_file)

    print(regs)
    lista_regs = regs['registros']
    registro = lista_regs[1]
    nome = registro['Nome']
    print(regs['registros'][0]['Nome'])
    print(nome)

if __name__ == '__main__':
    main()
