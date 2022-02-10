from datetime import date, timedelta
import requests # for mocking


class Student:
    '''
    A student class as base for method testing
    '''
    def __init__(self, first_name, last_name):
        '''
        The underscore on firstname and lastname is to signify
        that these fields are read only, As we want these to be read-only
        fields, we can prepend the first_name and last_name properties
        with an underscore so  other developers know how it should be used
        '''
        self._first_name = first_name
        self._last_name = last_name
        self._start_date = date.today()
        self.end_date = date.today() + timedelta(days=365)
        self.naughty_list = False

    @property
    def full_name(self):
        return f"{self._first_name} {self._last_name}"

    def alert_santa(self):
        self.naughty_list = True

    @property
    def email(self):
        return f"{self._first_name.lower()}.{self._last_name.lower()}@email.com" # noqa
    
    # def apply_extension(self,days):                -- my code but was incorrect # noqa
    #     return self.end_date + timedelta(days)     -- my code but was incorrect # noqa

    def apply_extension(self, days):
        self.end_date += timedelta(days=days)

    # for mocking
    def course_schedule(self):
        response = requests.get(f"http://company.com/course_schedule/{self._last_name}/{self._first_name}") # noqa

        if response.ok:
            return response.text
        else:
            return "Something went wrong with the request!"