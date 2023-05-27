import unittest

from calculator import evaluate

class BaseConversorTest(unittest.TestCase):
    def setUp(self) -> None:
        pass

    def test_basic(self):
        self.assertEqual(evaluate("+ 1 2"), 3)
        self.assertEqual(evaluate("* 1 2"), 2)
        self.assertEqual(evaluate("- 1 2"), -1)
        self.assertEqual(evaluate("/ 1 2"), 0.5)
        self.assertEqual(evaluate("+ 2 / 1 2"), 2.5)

    def test_malformed(self):
        with self.assertRaises(ValueError):
            evaluate("+ 2")

    def test_division_by_zero(self):
        with self.assertRaises(ValueError):
            evaluate("/ 2 0")

    def test_evaluate_addition(self):
        result = evaluate("+ 2 3")
        self.assertEqual(result, 5.0)
    
    def test_evaluate_subtraction(self):
        result = evaluate("- 7 4")
        self.assertEqual(result, 3.0)
    
    def test_evaluate_multiplication(self):
        result = evaluate("* 5 2")
        self.assertEqual(result, 10.0)
    
    def test_evaluate_division(self):
        result = evaluate("/ 12 3")
        self.assertEqual(result, 4.0)
    
    def test_evaluate_invalid_expression(self):
        with self.assertRaises(ValueError):
            evaluate("+ 2 3 *")
    
    def test_evaluate_division_by_zero(self):
        with self.assertRaises(ValueError):
            evaluate("/ 4 0")
    
    def test_evaluate_single_number(self):
        result = evaluate("5")
        self.assertEqual(result, 5.0)
    
    def test_evaluate_complex_expression(self):
        result = evaluate("- + * 2 3 / 4 2 1")
        self.assertEqual(result, 7.0)
if __name__ == '__main__':
    unittest.main()