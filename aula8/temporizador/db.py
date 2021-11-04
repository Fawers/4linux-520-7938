import sqlite3

def criar_tabela():
    conn = sqlite3.connect('timers.db')
    conn.execute('''CREATE TABLE IF NOT EXISTS timers (
        inicio INTEGER,
        duracao INTEGER,
        concluido INTEGER
    )''')
    conn.commit()
    conn.close()

def criar_timer(timer):
    conn = sqlite3.connect('timers.db')
    cur = conn.execute(f"""INSERT INTO timers VALUES
        ({int(timer.inicio.timestamp())},
        {int(timer.duracao.total_seconds())},
        0);""")
    conn.commit()
    conn.close()
    return cur.lastrowid


def concluir_timer(id):
    conn = sqlite3.connect('timers.db')
    conn.execute(f"UPDATE timers SET concluido = 1 WHERE rowid = {id}")
    conn.commit()
    conn.close()


def listar_todos():
    conn = sqlite3.connect('timers.db')
    cur = conn.execute(f"SELECT * FROM timers;")
    res = cur.fetchall()
    conn.close()

    return res


criar_tabela()
