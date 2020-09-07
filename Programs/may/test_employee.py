# Write your code here :-)
import unittest
from class_learning import employee

class TestEmployee(unittest.TestCase):

    def test_employee(self):

        emp1 = employee('srinu','b',65000)
        emp2 = employee('sow','a', 65000)

        self.assertEqual(emp1.email, 'srinub@.com')
        self.assertEqual(emp2.email, 'sowa@.com')


if __name__ == '__main__':
    unittest.main()
