import pymongo

client = pymongo.MongoClient()
db = client.caixa_eletronico


def login(username, senha):
    busca = {'username': username, 'senha': senha}
    admin = db.admins.find_one(busca)

    if admin is not None:
        return admin

    busca.pop('senha')
    cliente = db.clientes.find_one(busca)

    if cliente is None:
        return None

    if senha == cliente['senha']:
        if not cliente['bloqueado']:
            return cliente

        else:
            return None

    cliente['tentativas_erradas'] += 1

    if cliente['tentativas_erradas'] >= 3:
        cliente['bloqueado'] = True

    db.clientes.replace_one(busca, cliente)
    return None


def inserir_usuario(usuario):
    if 'conta' in usuario:
        if db.clientes.count_documents({'username': usuario['username']}) != 0:
            return None
        return db.clientes.insert_one(usuario).inserted_id

    else:
        if db.admins.count_documents({'username': usuario['username']}) != 0:
            return None
        return db.admins.insert_one(usuario).inserted_id


def atualizar_usuario(usuario):
    filtro = {'username': usuario['username']}
    return db.clientes.replace_one(filtro, usuario).acknowledged


def criar_root():
    if db.admins.count_documents({'username': 'root'}) != 0:
        print("Usuário root já existe")
        return

    res = db.admins.insert_one({'username': 'root', 'senha': 'root'})

    if res.acknowledged:
        print("Usuário root criado com sucesso.")

    else:
        print('Não foi possível criar o usuário root.')


criar_root()
