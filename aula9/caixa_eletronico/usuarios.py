from db import usuarios

class Usuario:
    def __init__(self, username, senha, _id=None):
        self.__username = username
        self.__senha = senha
        self.__id = _id

    @classmethod
    def login(cls, username, senha):
        dados = usuarios.login(username, senha)

        if dados is None:
            return None

        if 'conta' in dados:
            return Cliente(**dados)

        else:
            return Admin(**dados)

class Cliente(Usuario):
    def __init__(self, username, senha, bloqueado=True,
                 tentativas_erradas=0, primeiro_acesso=True,
                 conta=None, _id=None):
        super().__init__(username, senha, _id)
        self.__bloqueado = bloqueado
        self.__tentativas_erradas = tentativas_erradas
        self.__primeiro_acesso = primeiro_acesso

        if conta is None:
            conta = {'saldo': 0.0}

        self.__conta = conta

    def bloqueado(self):
        return self.__bloqueado

    def desbloquear(self):
        self.__bloqueado = False
        self.__primeiro_acesso = True
        self.resetar_tentativas_erradas()
        self.alterar_senha(self.__username)

    def primeiro_acesso(self):
        return self.__primeiro_acesso

    def incrementar_tentativas_erradas(self):
        self.__tentativas_erradas += 1
        return self.__tentativas_erradas

    def resetar_tentativas_erradas(self):
        self.__tentativas_erradas = 0

    def alterar_senha(self, senha):
        self.__senha = senha

    def get_saldo(self):
        return self.__conta['saldo']

    def sacar(self, quantia):
        saldo = self.__conta['saldo']

        if saldo < quantia:
            return None

        novo_saldo = saldo - quantia
        self.__conta['saldo'] = novo_saldo
        return novo_saldo

    def depositar(self, quantia):
        if quantia <= 0:
            return None

        self.__conta['saldo'] += quantia
        return self.__conta['saldo']

    def transferir(self):
        return self.__conta['saldo']

class Admin(Usuario):
    def cadastrar_cliente(self, username):
        c = Cliente(username, username)
        dados = {}

        for (k, v) in vars(c).items():
            k_ = k.replace('_Cliente__', '')\
                  .replace('_Usuario__', '')
            dados[k_] = v

        dados.pop('id')
        print(dados)
        id = usuarios.inserir_usuario(dados)
        c.__id = id

    def desbloquear_cliente(self, cliente):
        cliente.desbloquear()

