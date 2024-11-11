# Este archivo puede usarse como template para testear funciones. 
import unittest
"""from funciones import sumar  # Reemplazar por el import correspondiente para testear las funciones deseadas

# La clase puede tener otro nombre pero es necesario mantener el unittest.TestCase
class FuncionesTest(unittest.TestCase):

    # Definimos uno o más casos de test
    def test_1(self): #importante que empiece con "test"
        self.assertEqual(sumar(28,1), 29, "primer test") 

    def test_2(self):
        self.assertEqual(sumar(5,-2), 3, "segundo test")

if __name__ == '__main__':
    unittest.main(verbosity=2)

"""
from funciones import triangle # Reemplazar por el import correspondiente para testear las funciones deseadas

# La clase puede tener otro nombre pero es necesario mantener el unittest.TestCase
class FuncionesTest(unittest.TestCase):

    # Definimos uno o más casos de test
    def test_1(self): #importante que empiece con "test"
        self.assertEqual(triangle(-1,9,4), 4, "invalido") 

    def test_2(self):
        self.assertEqual(triangle(2,3,8), 4, "invalido")

    def test_3(self):
        self.assertEqual(triangle(9,9,9), 1, "equilatero")

    def test_4(self):
        self.assertEqual(triangle(2,2,1), 2, "isosceles")

    def test_5(self):
        self.assertEqual(triangle(4,8,2), 3, "escaleno")

if __name__ == '__main__':
    unittest.main(verbosity=2)
