from random import *  # má prática; não use
import time


print(randint(0, 30))
print(randint)

if randint.__module__ == 'random':
    print("vem do random")

print("antes do sleep")
time.sleep(1)
print("depois do sleep")

import ex_cadeiras
