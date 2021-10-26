import csv

def main():
    nome_arq = 'dados.csv'

    with open(nome_arq, 'a') as a:
        escrivao = csv.writer(a, delimiter=';')

        escrivao.writerow(['4', 'Harry Potter', 20, 'B', 'Inglês'])
        escrivao.writerows([
            ['555555', 'Bilbo Bolseiro', 40, 'H', 'Terra-medianês'],
            ['trevas', 'Batman', 'trevas', 'T', 'Gothanês']
        ])


if __name__ == '__main__':
    main()
