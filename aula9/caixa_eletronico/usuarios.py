from db import usuarios

class Usuario:
    def __init__(self, username, senha, _id=None):
        self.__username = username
        self.__senha = senha
        self.__id = _id

    def alterar_senha(self, nova_senha):
        self.__senha = nova_senha

    def resetar_senha(self):
        self.alterar_senha(self.__username)

    def salvar(self):
        dados = {}

        for (k, v) in vars(self).items():
            k_ = k.rpartition('__')[2]
            if k_ != 'id':
                dados[k_] = v

        if self.__id is not None:
            dados['_id'] = self.__id
            return usuarios.atualizar_usuario(dados)

        else:
            self.__id = usuarios.inserir_usuario(dados)
            return self.__id is not None

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
        self.resetar_senha()

    def primeiro_acesso(self):
        return self.__primeiro_acesso

    def incrementar_tentativas_erradas(self):
        self.__tentativas_erradas += 1
        return self.__tentativas_erradas

    def resetar_tentativas_erradas(self):
        self.__tentativas_erradas = 0

    def get_saldo(self):
        return self.__conta['saldo']

    def sacar(self, quantia):
        saldo = self.__conta['saldo']

        if saldo < quantia or quantia < 0:
            return None

        novo_saldo = saldo - quantia
        self.__conta['saldo'] = novo_saldo
        return novo_saldo

    def depositar(self, quantia):
        if quantia <= 0:
            return None

        self.__conta['saldo'] += quantia
        return self.__conta['saldo']

    def transferir(self, destinatario, quantia):
        novo_saldo_rem = self.sacar(quantia)

        if novo_saldo_rem is None:
            return None

        novo_saldo_dest = destinatario.depositar(quantia)
        return (novo_saldo_rem, novo_saldo_dest)

class Admin(Usuario):
    def cadastrar_cliente(self, username):
        return Cliente(username, username).salvar()

    def desbloquear_cliente(self, cliente):
        cliente.desbloquear()
        return cliente.salvar()

