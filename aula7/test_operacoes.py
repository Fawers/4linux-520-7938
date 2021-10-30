import unittest

import operacoes


class TestOperacoes(unittest.TestCase):
    def test_soma(self):
        esperado = 5
        real = operacoes.somar(2, 3)
        self.assertEqual(esperado, real)


if __name__ == '__main__':
    unittest.main()
