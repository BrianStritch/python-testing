def even_number_of_evens(numbers):
    """        LIST OF TEST IDEAS
    should raise a TypeError with an error message if a list
        isn't passed in as an argument.
    Error message: "A list was not passed into the function"
    If numbers is empty return False
    if numbers of even is odd return False
    if number of evens is zero return False
    if the numbers of evens is even return True


    numbered order is from refactoring
    """
    # return None  changed to true to make test pass
    # return True
    # this next conditional is to raise a typerror if a list is not passed to function
    if isinstance(numbers, list):
        # return True
        # this next conditional checks for asn empty list passed to function
        # if numbers == []:   1.  this line was removed for refactoring
        #     return False    1.  this line was removed for refactoring

            

        # else:               1.   this line was removed for refactoring

            # return True this was the return value for even numbers in list
            # for loop to check if number of even numbers in list is even amount
            # 7. evens = 0 # this variable was reassigned below after refactoring
            
            # 2. added in stage 2 of refactoring prints numbers in list
            # print([n for n in numbers])    

            # 3. changes number to 1 for each iteration prints [1,1,1]
            # print([1 for n in numbers])    

            # 4. added if statement to check divisible by 2
            # print([1 for n in numbers if n % 2 == 0])   

            # 5. wrap list comprehension in sum method to get total
            # print(sum([1 for n in numbers if n % 2 == 0]))

            # 6. evens variable reassigned to list compehension above for refactoring and print removed
            evens = sum([1 for n in numbers if n % 2 == 0])

            # 8. this was removed for refactoring as statement above replaces it
            # for n in numbers:
            #     if n % 2 == 0:
            #         evens += 1

            # 9. this was refactored as per below
            # this conditional tests to see if evens is equal to zero and returns the appropriate value # noqo
            # if evens: # this is the same as writing if evens > 0: as evens is True if greater than zero 
            #     return evens % 2 == 0
            # else:
            #     return False
            return True if evens and evens % 2 == 0 else False # checks for condition of evens if true or greater than zero

    else:
        raise TypeError("A list was not passed into the function")

# this code block when finnished should look like:
# def even_number_of_evens(numbers):
    """        LIST OF TEST IDEAS
    should raise a TypeError with an error message if a list
        isn't passed in as an argument.
    Error message: "A list was not passed into the function"
    If numbers is empty return False
    if numbers of even is odd return False
    if number of evens is zero return False
    if the numbers of evens is even return True
    """
#     if isinstance(numbers, list):
#         evens = sum([1 for n in numbers if n % 2 == 0])
#         return True if evens and evens % 2 == 0 else False
#     else:
#             raise TypeError("A list was not passed into the function")



'''
When the test was run this function call was also run.
Let’s prevent that from happening by making  the following change.
So what is this doing? To keep it  simple, when Python runs a file directly,
it names it __main__ and any code  beneath the if statement will only be run
if the name of the file is __main__.
'''


if __name__ == '__main__':
    # print(even_number_of_evens(5)) # removed in stage 2 of refactoring
    even_number_of_evens([2,1,4]) # added in stage 2 of refactoring
