"""   notes for the file
to run this file you use python3 test_evens.py

the reason why you use the pass statement is that Python is expecting an
indented block after the use of a colon, so when you have no code, using
the pass statement is valid and allows your code to run error free.

#2 import the class from the evens.py file for testing purposes

"""

import unittest
# 2
from evens import even_number_of_evens


class TestEvens(unittest.TestCase):
    # pass
    # def test_function_returns_true(self):  initial test
    #     self.assertTrue(even_number_of_evens([]))
    def test_throws_error_if_value_passed_in_is_not_list(self):
        self.assertRaises(TypeError, even_number_of_evens, 4)

    def test_values_in_list(self):
        # function to check for empty list passed as a list
        self.assertEqual(even_number_of_evens([]), False) # false is the expected return
        # function to check for two even numbers passed as a list
        self.assertEqual(even_number_of_evens([2,4]), True) # True is the expected return
        # function to check if only one even number passed as a list
        self.assertEqual(even_number_of_evens([2]), False) # False is the expected return
        # function to check if odd numbers passed as a list
        self.assertEqual(even_number_of_evens([1,3,5]), False) # False is the expected return



if __name__ == '__main__':
    unittest.main()
