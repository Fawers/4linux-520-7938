from datetime import datetime, timedelta
from time import sleep

import db


class Timer:
    def __init__(self, duracao):
        self.duracao = duracao

    def start(self):
        self.inicio = datetime.now()
        id = db.criar_timer(self)
        segundos = int(self.duracao.total_seconds())

        for s in range(1, segundos+1):
            sleep(1)
            print('.', end='', flush=True)

            if s % 10 == 0:
                print()

            if s % 60 == 0:
                print()

        print()
        db.concluir_timer(id)

    @classmethod
    def with_duration(cls, **delta):
        return Timer(timedelta(**delta))

    @classmethod
    def until_date(cls, data_fim):
        return cls(data_fim - datetime.now())

    @classmethod
    def list_all(cls):
        timers = db.listar_todos()

        for (i, d, c) in timers:
            inicio = datetime.fromtimestamp(i)
            duracao = timedelta(seconds=d)
            concluido = bool(c)

            print(inicio, duracao,
                  {True: "concluido", False: "não concluido"}[concluido])

Timer.with_duration(minutes=15).start()
# Timer.list_all()
