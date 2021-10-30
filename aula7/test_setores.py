import unittest

import setores

class TestSetores(unittest.TestCase):
    def test_colaboradores_financeiro_20(self):
        esperado = 20
        real = setores.get_colaboradores_do_setor('financeiro')
        self.assertEqual(esperado, real)

    def test_get_colaboradores_raises(self):
        self.assertRaises(
            setores.SetorInvalido,
            setores.get_colaboradores_do_setor,
            'contas')

    def test_tecnologia_no_andar_0(self):
        esperado = 'tecnologia'
        real = setores.get_setor_do_andar(0)
        self.assertEqual(esperado, real)

    def test_andar_invalido(self):
        self.assertRaises(
            setores.AndarInvalido,
            setores.get_setor_do_andar,
            -1)


if __name__ == '__main__':
    unittest.main()
