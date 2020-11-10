from Lab5.fracs import *
import unittest


class TestFractions(unittest.TestCase):

    def setUp(self):
        self.zero = [0, 1]

    def test_add_frac(self):
        self.assertEqual(add_frac([1, 2], [1, 3]), [5, 6])

    def test_sub_frac(self):
        self.assertEqual(sub_frac([5, 6], [1, 3]), [1, 2])

    def test_mul_frac(self):
        self.assertEqual(mul_frac([1, 2], [1, 3]), [1, 6])

    def test_div_frac(self):
        self.assertEqual(div_frac([1, 4], [4, 2]), [1, 8])

    def test_is_positive(self):
        self.assertEqual(is_positive([-1, 4]), False)
        self.assertEqual(is_positive([1, -4]), False)
        self.assertEqual(is_positive([-1, -4]), True)
        self.assertEqual(is_positive([1, 4]), True)

    def test_is_zero(self):
        self.assertEqual(is_zer0(self.zero), True)
        self.assertEqual(is_zer0([0, -1]), True)
        self.assertEqual(is_zer0([1, -1]), False)
        self.assertEqual(is_zer0([2, -1]), False)

    def test_cmp_frac(self):
        self.assertEqual(cmp_frac([1,4],[1,4]),0)
        self.assertEqual(cmp_frac([2,4],[1,2]),0)
        self.assertEqual(cmp_frac([1,4],[2,32]),1)
        self.assertEqual(cmp_frac([3,8],[1,2]),-1)

    def test_frac2float(self):
        self.assertEqual(frac2float([1, 2]), [1.0, 2.0])

    def tearDown(self):
        self.zero = None


if __name__ == '__main__':
    unittest.main()
