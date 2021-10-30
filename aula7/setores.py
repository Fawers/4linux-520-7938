setores = {
    'tecnologia': {
        'andar': 0,
        'colaboradores': 5
    },
    'rh': {
        'andar': 1,
        'colaboradores': 5
    },
    'financeiro': {
        'andar': 2,
        'colaboradores': 20
    }
}

# Todas as Exceptions possuem um atributo chamado args.
# Por isso não precisamos necessariamente definir o corpo das nossas
# classes.
class SetorInvalido(Exception):
    pass

class AndarInvalido(Exception):
    pass


def get_colaboradores_do_setor(setor):
    try:
        return setores[setor]['colaboradores']

    except KeyError:
        si = SetorInvalido(setor, setores.keys())
        # Quando passamos  ^^^^^  ^^^^^^^^^^^^^^
        # estas variáveis para a exceção, elas são
        # salvas no atributo args da exceção.
        raise si

def get_setor_do_andar(andar):
    for (setor, info_setor) in setores.items():
        if info_setor['andar'] == andar:
            return setor

    raise AndarInvalido(andar, (0, 2))

def main():
    print(get_colaboradores_do_setor('financeiro'))

    try:
        print(get_colaboradores_do_setor('video-jogos'))

    except SetorInvalido as si:
        # Essa variável     ^^
        # é o objeto SetorInvalido que criamos quando escrevemos
        # raise SetorInvalido(...) na linha 31.
        (setor_requisitado, setores_validos) = si.args
        # E quando referenciamos si.args aqui  ^^^^^^^
        # conseguimos acessar `setor` e `setores.keys()` passados
        # na linha 31.
        print("setor não existe:", setor_requisitado)
        print("setores válidos:", ', '.join(setores_validos))

    print(get_setor_do_andar(0))

    try:
        print(get_setor_do_andar(3))

    except AndarInvalido as ai:
        (andar_requisitado, (andar_i, andar_f)) = ai.args
        print("andar não existe:", andar_requisitado)
        print(f"tente entre {andar_i} e {andar_f}")

    try:
        raise AndarInvalido

    except AndarInvalido as ai:
        print(repr(ai))
