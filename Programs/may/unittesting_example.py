# Write your code here :-)
import random_functions
import unittest

class Testfunc(unittest.TestCase):

    def test_add(self):
        result = random_functions.add(10,5)
        self.assertEqual(result,15)


if __name__ == '__main__':
    unittest.main()
