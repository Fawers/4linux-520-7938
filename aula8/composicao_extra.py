class Compositora:  # A
    def __init__(self, obj_composta=None):
        if obj_composta is None:
            obj_composta = Composta()

        self.composta = obj_composta


class Composta:  # B
    pass


b = Composta()
a = Compositora(b)
a2 = Compositora()

print(b)
print(a, vars(a))
print(a2, vars(a2))
