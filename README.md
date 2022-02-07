# __PYTHON TESTING WITH UNITEST__
    - In this lesson, you will learn more about the  Unittest testing framework and see how tests  
            run successfully in preparation for a more  in-depth look at how the framework is used.
            Python provides us with a batteries-included  test module that is part of the Python standard library.
            This testing framework  is called Unittest.

            “Batteries-included” simply means that it comes with everything needed for full usability as standard.

    - Let's go over what we expect the  function we are going to build should do.

            We are going to write a function  that accepts a list of numbers and returns true if the list contains  an even number of even numbers. 

            It should also raise a TypeError if anything  other than a list is passed into the function.

So let’s pause for a moment and  think about what we should test for?            
And this is something you should always  do, even if you are not writing tests.

Ok, this is what I’ve (the instructor) come up with.

        - Our function should raise a TypeError with an error message if a list isn't passed in as an argument.

            It should return False when numbers is empty, the numbers of even is odd,and when the number of evens is zero.

            We'd expect it to return True if the numbers of evens is even, however.

So with this list of ideas for tests, I think we  are ready to get started setting up our files.
# __Stage 1__ 

### __create basic files__
    - create evens.py to write our python files
    - create test_evens.py to write test functions

#### __Setting up unittest__
    - Unittest requires that our test  filename starts with the word ‘test’,  
        followed by an underscore and a  descriptive name of what we’re testing.
        Next, we need to import the Unittest  module into our test_evens.py file.
        To do this, we simply type import Unittest.  
        As mentioned before, Unittest is part of Python’s  standard library, so we don’t need to install it.
        We are now ready to create a test case

#### __test_evens.py__
    - we'll do so by creating a class named TestEvens.
        To make use of Unittest’s functionality,  
        our class needs to inherit  from the unittest.TestCase class.
        I'll also add a pass statement and unittest.main. So we can run the file without specifying the unit test module.
        And when we run the code using the command python3  test_evens.py everything works fine, and we are  
        shown in the output that 0 tests were run, which  is fine as we have not created any tests yet. 
        You might be wondering what the pass statement does?  Let's comment it out and run the code again.
        You will see you get an error. Python is expecting  an indented block after the use of a colon,  
        so when you have no code using the pass statement  is valid and allows your code to run error free.
        
#### __evens.py__        
    - Let’s move over to our other file and  declare our function. I will name it  
        even_number_of_evens and give it a parameter  named numbers and have it return None.
        Underneath it, inside a print method, I will call it and pass it the value five.
        When I run this code, I see that our function works and returns None.
        
    - I am also going to add our list of test ideas to our function as a doc string, so we can refer to that if we need a
        reminder of what we could be testing for. 

#### __back to test_evens.py to set up first test__
    - I want to show a couple of more points  before we start building up our function  
        using unit testing, so I will do a  basic test to show how they work.
        First, we need to import our function into our test file.
        Now we can write a test to check  everything works and our setup is correct.
        So let's create a basic test that tests  whether if our function returns True.   
        It will be a method and needs to start with the word ‘test’.  If we don’t start the method name with the word test,
        it will be ignored and won't run, when we run the test file.
        And as we are in a class we need to pass in the self keyword.
        In here, we can create either a single assert or many asserts,  
        for now we will just create one just to show you how things work.
        So I’ll assertTrue that calling the function even_number_of_evens  
        with an empty list returns True. 
        If I run the test, we can see from the output  our test failed and the reason it failed. 

    - It states an AssertionError None is not True. This makes sense as our  
        function is set to return None, it also tells us  the line number and points to the test that fails,  
        which makes it handy to figure  out which test is failing.

    - When the test was run this function call was also run.
        Let’s prevent that from happening by making  the following change.
        So what is this doing? To keep it  simple, when Python runs a file directly,  
        it names it __main__ and any code  beneath the if statement will only be run  
        if the name of the file is __main__.
        
    - So when we run the test file it will have  the name __main__ and this code won't run.  
        But when we run this file it will have the  name __main__ and it will run this code.
        Let’s also add this to our  test file and then try it out.
        And we no longer see “True” in the output.

Okay, I’m going to change the True back to None, and delete our test in the test file 
and add back in the pass statement.
### __END OF STAGE 1__
And we're all set up for the next lesson, in which we create a working function incrementally,
by creating tests which should initially fail, and then pass by adding code to our function.
We also have a list of ideas for which tests we can create. See you there!

















































