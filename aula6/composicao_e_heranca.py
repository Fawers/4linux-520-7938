class Motor:
    def __init__(self, transmissao, tanque):
        self.transmissao = transmissao
        self.tanque = tanque
        self.velocidade = 0
        self.ligado = False

    def ligar(self):
        if not self.ligado:
            self.ligado = True

    def desligar(self):
        self.ligado = False
        self.velocidade = 0
        self.transmissao.ponto_morto()

class Transmissao:
    NEUTRO = 0

    def __init__(self, num_marchas):
        self.marchas = num_marchas
        self.marcha_atual = self.NEUTRO

    def alterar_marcha(self, nova_marcha):
        if 1 <= nova_marcha <= self.marchas:
            self.marcha_atual = nova_marcha
            return nova_marcha

        return self.marcha_atual

    def ponto_morto(self):
        self.marcha_atual = self.NEUTRO

class Acelerador:
    def __init__(self, motor):
        self.motor = motor

    def acelerar(self):
        if (self.motor.ligado
            and self.motor.transmissao.marcha_atual != Transmissao.NEUTRO):
            self.motor.velocidade += 1
            return True

        return False

class Freio:
    def __init__(self, motor):
        self.motor = motor

    def frear(self):
        if (self.motor.velocidade > 0):
            self.motor.velocidade -= 1
            return True

        return False

class Tanque:
    def __init__(self, capacidade):
        self.capacidade = capacidade
        self.volume_atual = 0

class Veiculo:
    def __init__(self, num_marchas, cap_tanque):
        self.tanque = Tanque(cap_tanque)
        self.motor = Motor(Transmissao(num_marchas), self.tanque)
        self.acelerador = Acelerador(self.motor)
        self.freio = Freio(self.motor)

    def ligar(self):
        self.motor.ligar()

    def desligar(self):
        self.motor.desligar()

    def acelerar(self):
        return self.acelerador.acelerar()

    def frear(self):
        return self.freio.frear()

    def marcha_atual(self):
        return self.motor.transmissao.marcha_atual

    def velocidade_atual(self):
        return self.motor.velocidade

    def subir_marcha(self):
        marcha_atual = self.motor.transmissao.marcha_atual
        nova_marcha = marcha_atual + 1
        return self.motor.transmissao.alterar_marcha(nova_marcha)

    def descer_marcha(self):
        return self.motor.transmissao.alterar_marcha(
            self.motor.transmissao.marcha_atual - 1)

    def abastecer(self, volume):
        vatual = self.tanque.volume_atual

        if vatual + volume >= self.tanque.capacidade:
            novo_volume = self.tanque.capacidade - vatual

        self.tanque.volume_atual += volume

class VeiculoAutomatico(Veiculo):
    def acelerar(self):
        super().acelerar()

        if self.velocidade_atual() % 5 == 1:
            self.subir_marcha()

    def frear(self):
        super().frear()

        if self.velocidade_atual() % 5 == 4:
            self.descer_marcha()

def main2():
    t1, t2 = Transmissao(5), Transmissao(6)
    print("o mesmo obj?", t1 is t2)
    print("neutro do t1:", t1.NEUTRO)
    print("neutro do t2:", t2.NEUTRO)
    print("neutro global:", Transmissao.NEUTRO)
    Transmissao.NEUTRO = -1
    print("neutro do t1:", t1.NEUTRO)
    print("neutro do t2:", t2.NEUTRO)
    print(t1.marchas, t2.marchas)
    t1.marchas = 15
    print(t1.marchas, t2.marchas)
    print(vars(t1))
    print(vars(t2))


def main():
    carro = VeiculoAutomatico(num_marchas=5, cap_tanque=45)
    print("verificação:")
    print("motor:", carro.motor.ligado)
    print("marcha:", carro.marcha_atual())
    print("velocidade:", carro.velocidade_atual())
    print("consigo acelerar?", carro.acelerar())

    carro.ligar()
    print("acelerando...", carro.acelerar())
    print("engatando...", carro.subir_marcha())
    print("acelerando...")
    for _ in range(5):
        carro.acelerar()
    print(f"estamos trafegando a {carro.velocidade_atual()} u/t")
    print("engatando...", carro.subir_marcha())
    for _ in range(3):
        carro.acelerar()
    print(f"estamos trafegando a {carro.velocidade_atual()} u/t")

    print("obstáculo na pista!")
    for _ in range(4):
        carro.frear()
    print("marcha:", carro.descer_marcha())

    print("pista livre! tapetão!")

    for _ in range(3):
        for _ in range(5):
            carro.acelerar()
        carro.subir_marcha()

    print("marcha atual:", carro.marcha_atual())

    print("chegamos ao nosso destino. vamos parar...")

    while carro.velocidade_atual() != 0:
        carro.frear()

    carro.desligar()


if __name__ == '__main__':
    main()
