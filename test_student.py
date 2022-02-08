"""   notes for the file
to run this file you use python3 test_student.py



"""

import unittest
# 2
from student import Student


class TestStudent(unittest.TestCase):
    
    def test_full_name(self):
        student = Student('John', 'Doe')

        self.assertEqual(student.full_name, 'John Doe')


if __name__ == '__main__':
    unittest.main()
