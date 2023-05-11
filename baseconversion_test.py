import unittest

from baseconversion import B2Conversor, BaseConversor

class BaseConversorTest(unittest.TestCase):
    def setUp(self) -> None:
        pass

    def test_B2Conversor(self):
        conversor = B2Conversor()
        self.assertEqual(conversor.convert(0), "0")
        self.assertEqual(conversor.convert(1), "1")
        self.assertEqual(conversor.convert(5), "101")

    def test_B2ConversorBig(self):
        conversor = B2Conversor()
        self.assertEqual(conversor.convert(489449845), "11101001011000110100101110101")
        self.assertEqual(conversor.convert(123456789012345678901234567890123456789012345678901234567890), 
                         '10011101010101111010100000100111001001011110000011110011000100001011100111111100001111010010000110111100011000011011110110100100111001000110011001111111100011001011011001110001111110000101011010010')

    def test_BaseConversor_2(self):
        conversor = BaseConversor(2)
        self.assertEqual(conversor.convert(0), "0")
        self.assertEqual(conversor.convert(1), "1")
        self.assertEqual(conversor.convert(5), "101")
        self.assertEqual(conversor.convert(10), "1010")
        self.assertEqual(conversor.convert(42), "101010")
        with self.assertRaises(TypeError):
            conversor.convert(-1)

        self.assertEqual(conversor.convert(489449845), "11101001011000110100101110101")
        self.assertEqual(conversor.convert(123456789012345678901234567890123456789012345678901234567890), 
                         '10011101010101111010100000100111001001011110000011110011000100001011100111111100001111010010000110111100011000011011110110100100111001000110011001111111100011001011011001110001111110000101011010010')
                         
    def test_BaseConversor_10(self):
        conversor = BaseConversor(10)
        self.assertEqual(conversor.convert(0), "0")
        self.assertEqual(conversor.convert(1), "1")
        self.assertEqual(conversor.convert(5), "5")
        self.assertEqual(conversor.convert(10), "10")
        self.assertEqual(conversor.convert(15), "15")
        self.assertEqual(conversor.convert(16), "16")

    def test_BaseConversor_10(self):
        conversor = BaseConversor(16)
        self.assertEqual(conversor.convert(0), "0")
        self.assertEqual(conversor.convert(1), "1")
        self.assertEqual(conversor.convert(5), "5")
        self.assertEqual(conversor.convert(10), "A")
        self.assertEqual(conversor.convert(15), "F")
        self.assertEqual(conversor.convert(16), "10")
        self.assertEqual(conversor.convert(255), "FF")
        with self.assertRaises(TypeError):
            conversor.convert(-1)

    def test_base7_conversion(self):
        c = BaseConversor(7)
        self.assertEqual(c.convert(0), "0")
        self.assertEqual(c.convert(1), "1")
        self.assertEqual(c.convert(10), "13")
        self.assertEqual(c.convert(42), "60")
        self.assertEqual(c.convert(123456789), "3026236221")
        with self.assertRaises(TypeError):
            c.convert(-1)

    def test_error(self):
        conversor = BaseConversor(10)
        with self.assertRaises(TypeError):
            conversor.convert(-1)

if __name__ == '__main__':
    unittest.main()