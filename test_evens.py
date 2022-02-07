"""   notes for the file
to run this file you use python3 test_evens.py

the reason why you use the pass statement is that Python is expecting an indented block after the use of a colon,  
so when you have no code, using the pass statement is valid and allows your code to run error free.

#2 import the class from the evens.py file for testing purposes

"""

import unittest
#2
from evens import even_number_of_evens

class TestEvens(unittest.TestCase):
    pass
    # def test_function_returns_true(self):  initial test
    #     self.assertTrue(even_number_of_evens([]))

if __name__ == '__main__':
    unittest.main()

