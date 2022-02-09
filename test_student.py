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

    def test_alert_santa(self):
        student = Student('John', 'Doe')
        student.alert_santa()

        self.assertTrue(student.naughty_list)
    
    def test_email(self):
        student = Student('John', 'Doe')

        self.assertEqual(student.email, 'john.doe@email.com')



if __name__ == '__main__':
    unittest.main()
