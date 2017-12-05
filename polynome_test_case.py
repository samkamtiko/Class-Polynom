import unittest
from polynome.polynome import Polynome


class PolynomeTestCase(unittest.TestCase):
    def test_valid_init(self):
        p = Polynome(1, 2)
        self.assertIsNotNone(p)

    def test_negative_exponent_init(self):
        with self.assertRaises(Exception) as context:
            p = Polynome(1, -1)
        self.assertTrue('Exponent can not be negative: -1' in str(context.exception))

    def test_str_zero_polynome(self):
        p = Polynome(0)
        self.assertEqual(str(p), '0')

    def test_str_zero_degree_polynome(self):
        p = Polynome(5)
        self.assertEqual(str(p), '5')

    def test_str_high_degree_polynome(self):
        p = Polynome(5, 4)
        self.assertEqual(str(p), '5x^4')

    def test_equal_polynome(self):
        p = Polynome(4, 3) + Polynome(-3, 2) + Polynome(2, 1) + Polynome(-1)
        q = Polynome(4, 3) + Polynome(-3, 2) + Polynome(2, 1) + Polynome(-1)
        self.assertTrue(p == q)

    def test_not_equal_polynome(self):
        p = Polynome(4, 3) + Polynome(-3, 2) + Polynome(2, 1) + Polynome(-1)
        q = Polynome(4, 5) + Polynome(-3, 1) + Polynome(2, 1) - Polynome(-1)
        self.assertTrue(p != q)

    def test_equal_int(self):
        p = Polynome(5)
        q = int(5)
        self.assertTrue(p == q)

    def test_not_equal_int(self):
        p = Polynome(1, 2) + Polynome(5)
        q = int(5)
        self.assertTrue(p != q)

    def test_equal_float(self):
        p = Polynome(5.0)
        q = float(5)
        self.assertTrue(p == q)

    def test_not_equal_float(self):
        p = Polynome(1, 2) + Polynome(5)
        q = float(5)
        self.assertTrue(p != q)

    def test_equal_object(self):
        p = Polynome(4, 3) + Polynome(-3, 2) + Polynome(2, 1) + Polynome(-1)
        with self.assertRaises(NotImplementedError):
            res = p == list()

    def test_not_equal_object(self):
        p = Polynome(4, 3) + Polynome(-3, 2) + Polynome(2, 1) + Polynome(-1)
        with self.assertRaises(NotImplementedError):
            res = p != list()

    def test_lesser_polynome(self):
        p = Polynome(3, 3) + Polynome(-3, 2) + Polynome(2, 1) + Polynome(-1)
        q = Polynome(4, 3) + Polynome(-3, 2) + Polynome(2, 1) + Polynome(-1)
        self.assertLess(p, q)

    def test_greater_polynome(self):
        p = Polynome(-3, 2) + Polynome(2, 1) + Polynome(-1)
        q = Polynome(4, 3) + Polynome(-3, 2) + Polynome(2, 1) + Polynome(-1)
        self.assertGreater(q, p)

    def test_lesser_int(self):
        p = Polynome(-1)
        q = int(4)
        self.assertLess(p, q)

    def test_greater_int(self):
        p = Polynome(6)
        q = int(-1)
        self.assertGreater(p, q)

    def test_lesser_float(self):
        p = Polynome(-1)
        q = float(4.0)
        self.assertLess(p, q)

    def test_greater_float(self):
        p = Polynome(6.0)
        q = float(2.0)
        self.assertGreater(p, q)

    def test_lesser_object(self):
        p = Polynome(3, 3) + Polynome(-3, 2) + Polynome(2, 1) + Polynome(-1)
        q = list()
        with self.assertRaises(NotImplementedError):
            res = p < q

    def test_greater_object(self):
        p = Polynome(-1)
        q = list()
        with self.assertRaises(NotImplementedError):
            res = p > q

    def test_sum_polynome(self):
        p = Polynome(4, 3) + Polynome(-3, 2) + Polynome(2, 1) + Polynome(-1)
        self.assertEqual(str(p), '4x^3 - 3x^2 + 2x - 1')

    def test_sum_float(self):
        p = Polynome(2, 1) + int(1)
        self.assertEqual(str(p), '2x + 1')

    def test_sum_int(self):
        p = Polynome(2, 1) + float(1.5)
        self.assertEqual(str(p), '2x + 1.5')

    def test_sum_object(self):
        with self.assertRaises(NotImplementedError):
            p = Polynome(2, 1) + list()

    def test_sub_polynome(self):
        p = Polynome(3, 2) - Polynome(2, 1) - Polynome(1)
        self.assertEqual(str(p), '3x^2 - 2x - 1')

    def test_sub_float(self):
        p = Polynome(2, 1) - int(1)
        self.assertEqual(str(p), '2x - 1')

    def test_sub_int(self):
        p = Polynome(2, 1) - float(1.5)
        self.assertEqual(str(p), '2x - 1.5')

    def test_sub_object(self):
        with self.assertRaises(NotImplementedError):
            p = Polynome(2, 1) - list()

    def test_mul_polynome(self):
        p = Polynome(4, 3) + Polynome(3, 2) - Polynome(2, 1) + 1
        q = Polynome(3, 2) + 5
        self.assertEqual(str(p * q), '12x^5 + 9x^4 + 14x^3 + 18x^2 - 10x + 5')

    def test_mul_float(self):
        p = Polynome(4, 3) + Polynome(3, 2) + Polynome(2, 1) + 1
        self.assertEqual(str(p * 0.5), '2.0x^3 + 1.5x^2 + x + 0.5')

    def test_mul_int(self):
        p = Polynome(4, 3) + Polynome(3, 2) + Polynome(2, 1) + 1
        self.assertEqual(str(p * 2), '8x^3 + 6x^2 + 4x + 2')

    def test_mul_object(self):
        with self.assertRaises(NotImplementedError):
            p = Polynome(2, 1) * list()

    def test_compose_polynome(self):
        p = Polynome(4, 3) + Polynome(3, 2) + Polynome(2, 1) + 1
        q = Polynome(3, 2) + 5
        self.assertEqual(str(p(q)), '108x^6 + 567x^4 + 996x^2 + 586')

    def test_evaluate_int(self):
        p = Polynome(4, 3) + Polynome(3, 2) + Polynome(2, 1) + 1
        self.assertEqual(str(p(1)), '10')

    def test_evaluate_float(self):
        p = Polynome(4, 3) + Polynome(3, 2) + Polynome(2, 1) + 1
        self.assertEqual(str(p(0.5)), '3.25')

    def test_evaluate_object(self):
        with self.assertRaises(NotImplementedError):
            p = Polynome(4, 3) + Polynome(3, 2) + Polynome(2, 1) + 1
            p(list())


if __name__ == '__main__':
    unittest.main()
