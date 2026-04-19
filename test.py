import unittest
from app import add, sub, mul

class testmathfunctions(unittest.TestCase):
    def test_add(self):
        self.assertEqual(add(4, 5), 9)
        self.assertEqual(add(-1, 1), 0)
        self.assertEqual(add(0, 0), 0)

    def test_sub(self):
        self.assertEqual(sub(4, 1), 3)
        self.assertEqual(sub(5, 2), 3)
        self.assertEqual(sub(0, 0), 0)

    def test_mul(self):
        self.assertEqual(mul(4, 5), 20)
        self.assertEqual(mul(-1, 1), -1)
        self.assertEqual(mul(0, 10), 0)

if __name__ == '__main__':
    unittest.main()