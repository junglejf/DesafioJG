'''
    Módulo de Testes TDD
'''
import unittest
import util as jg
import sys
import rules as rl

class Testjg(unittest.TestCase):
    '''
    1 - test_jg_de_X -> que testa a função jovensgenios no valor X
    2 - setUp -> define um intervalo de testes no atributo num
    3 - test_jg_de_num testa todo intervalo de 3 até num da função jovensgenios
    '''
    def setUp(self):
        self.num = 1000

    def test_jg_de_0(self):
        self.assertEqual(jg.jovensgenios(0), 'JovensGênios')

    def test_jg_de_1(self):
        self.assertEqual(jg.jovensgenios(1), '1')

    def test_jg_de_2(self):
        self.assertEqual(jg.jovensgenios(2), '2')

    def test_jg_de_3(self):
        self.assertEqual(jg.jovensgenios(3), 'Jovens')

    def test_jg_de_5(self):
        self.assertEqual(jg.jovensgenios(5), 'Gênios')

    def test_jg_de_Negative(self):
        self.assertEqual(jg.jovensgenios(-1), '-1')

    def test_jg_de_15(self):
        self.assertEqual(jg.jovensgenios(15), 'JovensGênios')  

    def test_jg_de_num(self):
        num = self.num
        for i in range(15,num+1,15):
            self.assertEqual(jg.jovensgenios(i), 'JovensGênios')

        for i in range(5,num+1,5):
            self.assertIn('Gênios',jg.jovensgenios(i))

        for i in range(3,num+1,3):
            self.assertIn('Jovens', jg.jovensgenios(i)) 
            if not(rl.divisivel_por_5):
                self.assertEqual(jg.jovensgenios(i+1), str(i+1))   

		

if __name__ == '__main__':
    
	unittest.main()