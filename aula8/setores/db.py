setores = {
    'tecnologia': {
        'andar': 0,
        'colaboradores': 5
    },
    'rh': {
        'andar': 1,
        'colaboradores': 5
    },
    'financeiro': {
        'andar': 2,
        'colaboradores': 20
    }
}

import sqlite3


def criar_tabela(conn):
    # CREATE TABLE setores (
    #   nome TEXT,
    #   andar INTEGER,
    #   colaboradores INTEGER
    # );
    conn.execute("""
        CREATE TABLE IF NOT EXISTS setores (
            nome TEXT,
            andar INTEGER,
            colaboradores INTEGER
        )
    """)
    conn.commit()  # COMMIT


def inserir_dados(conn, dados):
    dados_fmt = []
    for (nome, andar, colab) in dados:
        dados_fmt.append(
            '('
            + ', '.join([repr(nome),
                             repr(andar),
                             repr(colab)])
            + ')'
        )

    query = f"""
        INSERT INTO setores VALUES
        {', '.join(dados_fmt)};
    """
    print(query)
    conn.execute(query)
    conn.commit()


def mostrar_tabela(conn):
    cursor = conn.execute("SELECT rowid, * FROM setores;")

    for linha in cursor:
        print(linha)

def main():
    conn = sqlite3.connect('db.sqlite3')
    criar_tabela(conn)
    inserir_dados(conn, [
        ("tecnologia", 0, 5),
        ("rh", 1, 5),
        ("financeiro", 2, 20),
    ])
    mostrar_tabela(conn)


if __name__ == '__main__':
    main()

# Setores
# Nome          : TEXT
# Andar         : INT
# Colaboradores : INT

# CREATE TABLE setores (
#   nome TEXT,
#   andar INTEGER,
#   colaboradores INTEGER
# );

# INSERT INTO setores VALUES
# ("tecnologia", 0, 5),
# ("rh", 1, 5),
# ("financeiro", 2, 20);

# SELECT nome, colaboradores FROM setores
# WHERE colaboradores = 5
# ORDER BY nome [ASC | DESC];

# INSERT INTO setores VALUES
# ("deposito", -1, 0);

# UPDATE setores SET colaboradores = 5 WHERE andar = -1;

# DELETE FROM setores WHERE nome = 'deposito';

# TRUNCATE TABLE setores; <-- não existe mais
# equivalente: DELETE FROM setores;

# DROP TABLE setores;
