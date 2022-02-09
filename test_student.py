"""   notes for the file
to run this file you use python3 test_student.py



"""
from datetime import date, timedelta
import unittest
# 2
from student import Student


class TestStudent(unittest.TestCase):

    @classmethod
    def setUpClass(cls):
        print('setUpClass')

    @classmethod
    def tearDownClass(cls):
        print('tearDownClass')

    def setUp(self):
        print('setup')
        self.student = Student('John', 'Doe')

    def tearDown(self):
        print('teardown')

    def test_full_name(self):
        print('test_full_name')
        self.assertEqual(self.student.full_name, 'John Doe')

    def test_alert_santa(self):
        print('test_alert_santa')
        self.student.alert_santa()
        self.assertTrue(self.student.naughty_list)

    def test_email(self):
        print('test_email')
        self.assertEqual(self.student.email, 'john.doe@email.com')

    # def test_apply_extension(self):             -- my code but was incorrect
    # i should have created the variable here
    #     self.student.apply_extension(5)         -- my code but was incorrect
    #     self.assertEqual(self.student.apply_extension, self.student.end_date + timedelta(days=5)) # noqa

    def test_apply_extension(self):
        old_end_date = self.student.end_date
        self.student.apply_extension(5)
        self.assertEqual(self.student.end_date, old_end_date + timedelta(days=5)) # noqa
        """
        - create a new test method called test_apply_extension
        - inside test_apply_extension, store the current end date
             for our test student instance in a variable called old_end_date

        - call a method named apply_extension that will take a number of days
             as an arguement on the student instance to update the end_date

        - assert whether the instance's end date equals the old end date plus
             the days arguement that was passed in using timedelta

        - run the tests to confirm that the new method is failing

        - in the student class, create a new method  called apply_extension
            that has a parameter called days

        - use the timedelta method from timeline to update the end_date 
            property

        - run the tests to confirm they are working


        The method below is also great!  But keep in mind that  it will
        only be correct if a student has received 1 extenstion.  If
        they receive a second - it would return false

        self.student.apply_extension(5)
        self.assertEqual(self.student.end_date, self.student._start_date 
                                                    + timedelta(days=370))
        """


if __name__ == '__main__':
    unittest.main()
