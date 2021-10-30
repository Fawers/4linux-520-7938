import unittest

from pilha_classes import Pilha


class TestPilha(unittest.TestCase):
    def test_pilha_com_limite_0_esta_cheia_e_vazia(self):
        p = Pilha(limite=0)
        self.assertTrue(p.cheia())
        self.assertTrue(p.vazia())

    def test_empilhar_1_em_pilha_com_limite_1_a_torna_cheia(self):
        p = Pilha(limite=1)
        p.empilhar('elemento')
        self.assertTrue(p.cheia())

    def test_desempilhar_quando_pilha_tem_apenas_1_a_torna_vazia(self):
        p = Pilha()
        p.empilhar('elemento')
        self.assertFalse(p.vazia())
        p.desempilhar()
        self.assertTrue(p.vazia())

    def test_topo_apos_empilhar_eh_o_elemento_empilhado(self):
        p = Pilha()
        p.empilhar(1)
        self.assertEqual(p.topo(), 1)
        p.empilhar(2)
        self.assertEqual(p.topo(), 2)
        p.empilhar(3)
        self.assertEqual(p.topo(), 3)
        p.empilhar(4)
        self.assertEqual(p.topo(), 4)

if __name__ == '__main__':
    unittest.main()
