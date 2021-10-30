import tratamento

def main():
    while True:
        try:
            dividendo = int(input('Digite o dividendo: '))
            divisor = int(input('Digite o divisor: '))
            return dividendo / divisor

        except Exception:
            print("exception")

        except ValueError:
            print("Digite um número válido!")

        except ZeroDivisionError:
            print("divisão por 0")

        except TypeError:
            print('boom')

        else:
            print("estou no else")

        finally:
            print("deu erro? estou no finally")
            return "finally"

print(main())
# print(tratamento.number_input('Digite um número: '))

# try:
#     f = open('um-arquivo.txt', 'w')
#     f.read()

# finally:
#     print("fechando arquivo...")
#     f.close()

# import sqlite3

# db = sqlite3.connect(':memory:')

# try:
#     db.execute('SELECT * FROM tabela;')

# except sqlite3.OperationalError:
#     print("boom")
