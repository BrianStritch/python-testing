def even_number_of_evens(numbers):
    """        LIST OF TEST IDEAS
    should raise a TypeError with an error message if a list
        isn't passed in as an argument.
    Error message: "A list was not passed into the function"
    If numbers is empty return False
    if numbers of even is odd return False
    if number of evens is zero return False
    if the numbers of evens is even return True
    """
    # return None  changed to true to make test pass
    # return True
    # this next conditional is to raise a typerror if a list is not passed to function
    if isinstance(numbers, list):
        # return True
        # this next conditional checks for asn empty list passed to function
        if numbers == []:
            return False 
            

        else:            
            # return True this was the return value for even numbers in list
            # for loop to check if number of even numbers in list is even amount
            evens = 0
            for n in numbers:
                if n % 2 == 0:
                    evens += 1
            # this conditional tests to see if evens is equal to zero and returns the appropriate value # noqo
            if evens: # this is the same as writing if evens > 0: as evens is True if greater than zero 
                return evens % 2 == 0
            else:
                return False

    else:
        raise TypeError("A list was not passed into the function")


'''
When the test was run this function call was also run.
Let’s prevent that from happening by making  the following change.
So what is this doing? To keep it  simple, when Python runs a file directly,
it names it __main__ and any code  beneath the if statement will only be run
if the name of the file is __main__.
'''


if __name__ == '__main__':
    print(even_number_of_evens(5))
