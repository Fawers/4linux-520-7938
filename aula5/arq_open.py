def read_image(arq_nome):
    with open(arq_nome, 'rb') as arq:
        primeiros_521B = arq.read(512)
        print(primeiros_521B)

def append_to_file(arq_nome):
    with open(arq_nome, 'a+') as arq:
        print(arq.readable())
        print(":)", file=arq)

def write_to_file(arq_nome):
    with open(arq_nome, 'w') as arq:
        print(arq.readable())
        arq.write(":")
        print(")", file=arq, end='\n\n')

def read_lines(arq_nome):
    with open(arq_nome) as arq:
        # print(arq.closed)
        linhas = arq.readlines()
        print(linhas)

    # print(arq.closed)

def read_line(arq_nome):
    arq = open(arq_nome)

    primeira_linha = arq.readline()
    print(primeira_linha, end='')
    print(primeira_linha.strip(), end='')

    arq.close()

def read_some(arq_nome):
    arq = open(arq_nome)

    primeiros_100 = arq.read(100)
    print(primeiros_100)

    arq.close()

def read_all(arq_nome):
    arq = open(arq_nome)

    if arq.readable():
        conteudo = arq.read()
        print(conteudo)
        print(conteudo.count("Hellraiser"))
        print(conteudo.upper().count("ROCK AND ROLL"))

    else:
        print("Não consigo ler o arquivo")

    arq.close()


if __name__ == '__main__':
    # read_all("hellraiser.txt")
    # read_some("hellraiser.txt")
    # read_line("hellraiser.txt")
    # read_lines("hellraiser.txt")
    # write_to_file("nome.txt")
    # append_to_file("nome.txt")
    read_image("python.jpg")
