import unittest
import fracs

class TestFractions(unittest.TestCase):

    def test_add_frac(self):
        self.assertEqual(fracs.add_frac([1, 2], [1, 3]), [5, 6])

    def test_sub_frac(self):
        self.assertEqual(fracs.sub_frac([9, 10], [4, 5]), [1, 10])

    def test_mul_frac(self):
        self.assertEqual(fracs.mul_frac([11, 7], [3, 4]), [33, 28])
        self.assertEqual(fracs.mul_frac([-11, 7], [3, 4]), [-33, 28])

    def test_div_frac(self):
        self.assertEqual(fracs.div_frac([11, 7], [3, 4]), [44, 21])

    def test_is_positive(self):
        self.assertTrue(fracs.is_positive([1, 2]))
        self.assertTrue(fracs.is_positive([-1, -2]))
        self.assertFalse(fracs.is_positive([-1, 2]))
        self.assertFalse(fracs.is_positive([1, -2]))

    def test_is_zero(self):
        self.assertTrue(fracs.is_zero([0, 2]))
        self.assertTrue(fracs.is_zero([0, 15]))
        self.assertFalse(fracs.is_zero([1, 2]))

    def test_cmp_frac(self):
        self.assertEqual(fracs.cmp_frac([1, 2], [8, 16]), 0)
        self.assertEqual(fracs.cmp_frac([7, 15], [9, 19]), -1)
        self.assertEqual(fracs.cmp_frac([1, 2], [7, 15]), 1)

    def test_frac2float(self):
        self.assertEqual(fracs.frac2float([1, 2]), 0.5)
        self.assertEqual(fracs.frac2float([4, 20000]), 0.0002)

if __name__ == '__main__':
    unittest.main()     # uruchamia wszystkie testy