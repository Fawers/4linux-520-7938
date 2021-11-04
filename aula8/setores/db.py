import sqlite3


def criar_tabela(conn):
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
    cursor = conn.execute(query)
    conn.commit()
    return cursor.lastrowid


def atualizar_dados(conn, atualizacoes, id):
    # atualizacoes = ["'nome' = 'deposito'", "", ...]
    query = f"UPDATE setores SET {', '.join(atualizacoes)} WHERE rowid = {id}"
    conn.execute(query)
    conn.commit()


def remover_dados(conn, id):
    query = f"DELETE FROM setores WHERE rowid = {id}"
    conn.execute(query)
    conn.commit()


def selecionar_dados(conn, colunas, id):
    query = f"SELECT {', '.join(colunas)}, rowid FROM setores WHERE rowid = {id};"
    return conn.execute(query).fetchone()


def selecionar_todos(conn, colunas):
    query = f"SELECT {', '.join(colunas)}, rowid FROM setores;"
    return conn.execute(query).fetchall()


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

