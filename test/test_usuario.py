
import unittest
import usuario

class UsuarioTest(unittest.TestCase):

    def testsaludardeberia(self):

        #argante
        saludoesperado = "hola"

        #ACT
        saludorecibido = usuario.saludar()

        #ASSERT
        self.assertEqual(saludoesperado,saludorecibido)

