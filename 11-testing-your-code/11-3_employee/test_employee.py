import unittest
from employee import Employee

class TestEmployee(unittest.TestCase):
    """Test for the class Employee"""

    def setUp(self):
        self.my_employee = Employee('John', 'Smith', 25)

    def test_give_default_bonus(self):
        self.my_employee.give_bonus()
        self.assertEqual(self.my_employee.bonus, 35)
        
    def test_give_custom_bonus(self):
        self.my_employee.give_bonus(25)
        self.assertEqual(self.my_employee.bonus, 50)

if __name__ == '__main__':
    unittest.main()