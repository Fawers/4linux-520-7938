import datetime

agora = datetime.datetime.now()
print(agora)
data_nasc = datetime.datetime(1992, 4, 4, 9, 47, 0)

delta = agora - data_nasc

print(delta)
print(delta.total_seconds())
