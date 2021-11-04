import sys
from time import sleep
from datetime import datetime, timedelta
from time import sleep

import db


class Timer:
    def __init__(self, duracao):
        self.duracao = duracao

    def create(self):
        return db.criar_timer(self)

    def conclude(self, id):
        db.concluir_timer(id)

    def start(self):
        self.inicio = datetime.now()
        id = self.create()
        segundos = int(self.duracao.total_seconds())

        for s in range(1, segundos+1):
            sleep(1)
            print('.', end='', flush=True)

            if s % 10 == 0:
                print()

            if s % 60 == 0:
                t = int(self.duracao.total_seconds() - s) // 60
                print(f'{t}M')

        print()
        self.conclude(id)

    @classmethod
    def with_duration(cls, **delta):
        return cls(timedelta(**delta))

    @classmethod
    def until_date(cls, data_fim):
        return cls(data_fim - datetime.now())

    @classmethod
    def get_all(cls):
        return db.listar_todos()

    @classmethod
    def list_all(cls):
        timers = cls.get_all()

        for (i, d, c) in timers:
            inicio = datetime.fromtimestamp(i)
            duracao = timedelta(seconds=d)
            concluido = bool(c)

            print(inicio, duracao,
                  {True: "concluido", False: "não concluido"}[concluido])

Timer.with_duration(minutes=15).start()
# Timer.list_all()
