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
