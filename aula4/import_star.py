from random import *  # má prática; não use


print(randint(0, 30))
print(randint)

if randint.__module__ == 'random':
    print("vem do random")
