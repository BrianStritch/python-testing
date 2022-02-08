from datetime import date, timedelta

class Student:
    '''
    A student class as base for method testing
    '''
    def __init__(self, first_name, last_name):
        ''' The underscore on firstname and lastname is to signify that these fields are read only,
        As we want these to be read-only fields, we can prepend the first_name  
        and last_name properties with an underscore so  other developers know how
        it should be used
        '''
        self._first_name = first_name 
        self._last_name = last_name
        self.start_date = date.today()
        self.end_date = date.today() + timedelta(days = 365)
        self.naughty_list = False

    @property
    def full_name(self):
        return f"{self._first_name} {self._last_name}"