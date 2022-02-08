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

# __Stage 2 - Building a function using TDD__
In our last stage, we had an  introduction to the Unittest testing framework.
We also set up our test file with the basic scaffolding required and we ran a test to  
see how things work. We created a file for our  function which we named even_number_of_evens  
and ran this to make sure all was working. Lastly,  we imported our function into our test file.
With all that sorted in the last stage, we  can start writing the first of our tests.

#### __testing for type - typerror testing__
    - One of the first items we want to test for is that a TypeError is raised if a list is not passed into  
        the function when it’s called. As mentioned in the previous stage, test functions need to start  
        with the word ‘test’. If they don’t, they’ll be  ignored and won’t be run when we run our tests. 

    - Let’s give our test a descriptive name that details what it is testing,  
        test_throws_error_if_value_passed_in_is_not_list,  and pass in a reference to self.
        - Inside our test, we write our assert  and I will use the assertRaises method.
           This will call the assertRaises method  from TestCase and when the test is run  
           it checks to see if a TypeError is raised  when the function is called with the value  
           4. This should fail, as our function  at the moment is set to return None.

Let’s run the test using the  command python3 test_evens.py. We can see from the output that  it did fail and the reason given  
is that a TypeError wasn’t  raised by even_number_of_evens. So we have a fail, which is what we  want initially when we create a test. We now need to write some code in our  function to get this test to pass.

##### __evens.py typeError testing__
    - I am going to add a check in our function  that checks if the value passed in is a list, 
        and if it is, return True else raise a TypeError.
        So I am going to replace the return statement,  
        write an if else statement, use the isinstance()  method to check if the value “numbers” is a list  
        and add a string to output  when the error is raised.

So let’s save that and go back to  our test file and run the test again.  
This time we can see we get a pass, indicated  by the . and Ok at the end of the output.
So to recap what we have done, we  first wrote a test that should fail  
and then we wrote code in our  function so that our test passes.  
This is the red and green parts  of our red-green-refactor cycle.

#### __test_evens.py - test for empty list passed into function__
    - The next test should test our  function returns False if an  
        empty list is passed in, so I’ll create  a new test named test_values_in_list,  
        and will use this code block  for the next few assertions.
        I need to write an assertion  that checks if an empty list  
        has been passed in and should be expecting False.
        For this test I will use the assertEqual  method passing in the function with an  
        empty list as an argument, and  the expected return of False.
        And when we run the tests, it fails as expected.  

##### __evens.py - test for empty list passed into functions__
    - Again we need to add to the code in our  function, just enough to pass the test.
        Let's pause so that you can think about what you  would need to add to the code in the function  
        to pass this test. We will walk through  how I would do it when you get back.
        Let’s look at how I got this test to pass.
        Back in the function, I will replace  the return True with an if statement,  
        which checks if numbers is equal to an  empty list and returns False if it is.

So let’s save the code and go back to  our test file and run the tests again.  
We can see from the output  that this has now passed.
So at this stage, you should understand the  process, which is you write a test that fails  
and then add code to the function  that should get the test to pass. Our test passes for an empty list.

#### __test_evens.py - test for two even values passed as list__
What  should it do if we pass in two even numbers?  
In this case, we would want it to pass.

    - So let’s add another assert that should pass  when we add two even numbers to the list.
        And when we run our test we see it fails.  

So, how do we get this to pass? 

##### __evens.py - test for two even values passed as list__

    - Let’s add  an else to our if statement and return True.

    - This is probably not what you were expecting but  if we save our code and run the tests, we can see  
        them all passing with flying colours. 

Looking at  the code in the function, it may seem that it does  
not make sense, but we are incrementally building  up the function by writing and passing tests.

#### __test_evens.py - testing if only one even number is passed__
Our function at the moment returns True for any  amount of numbers passed into it, and that's fine,  
but what is a test it should fail for? It should  fail if only one even number is passed in

    - so let's write a test that  checks for one even number.  
        This test will fail and we can then look  at what we need to do to get it to pass.
        Let’s run the tests. And as  expected this test fails.
        We’re at the stage now where we need to  count the number of even numbers in the list 
        and then check if that number itself is even.  So let's write the code to make this test pass.

##### __evens.py - testing if only one number passed__
    - If a number is sent in, let's initialize  a variable to say that we currently have zero evens.  
        And now, let's write a for loop 
        and within it an if statement that  checks if each number is even.

    - We can use the modulo operator to see if the  remainder when it's divided by two is zero. 
        If it is, then it's an even number  and we increment the evens variable.
        Outside the for loop, I’ll add a return  statement and using the modulo operator  
        check if the evens variable is an even number.
        So this will return True if the number  of evens is even, and False if it's not.
        
Let's save that and run the tests again and see what we get. And we can see that all tests are passing. 

#### __test_evens - testing for odd numbers in list__
Things are looking good. Our function is  generally working, but there are still more  
tests because we haven't tested what will happen if we send in any odd numbers yet. 

    - I’ll create another assert  so we can see what happens  
        if we send in an odd number of odd numbers.
        We would expect this to return  False but this time pass the test.  
        
Let's run our program. It fails! That means that our program was returning True when it should have been returning False. 

###### __test question from instructor__
Just have a look at the code for a  few minutes. See if you can figure  
out for yourself why the code is returning  True when it should be returning False. 
    - Well, as we see, the problem is here with our return in evens.py 
        Because we pass in 3 odd numbers, evens is going  to have the value 0 and 0 % 2 will equal 0,  
        so True is returned. What we need to do here  
        is add an if statement. We can use a truthy  falsy value check of evens, so if evens is > 0  
        it will evaluate to True and False if it is 0 And within the if evens is greater than 0,  
        we can return evens % 2 == 0.
        Now, when we run this, all tests are passed again.

### __end of stage 2__

We've used test-driven development to build  our function incrementally, and it works! 
It's not the prettiest, and it's maybe  not written using the cleanest code,  
but now that we know that it works, we can go  ahead and refactor our code with confidence. 
In our next lesson, that's exactly  what we're going to do. See you there!

# __Stage 3 - refactoring__
In the previous lesson, we created our function using unit testing and in this video,  
we are going to look at refactoring our code. Using the DRY, or Don't Repeat Yourself,  
principle, we can have a look at  our code and see if there's anything  
that's repetitive or redundant.

###### __refactoring step 1__
    -  One thing that stands out straight  
        away is our check for an empty list  right at the beginning of our code. 
        As we step through the code, we can see that our  check to see if evens equals 0 should cover that,  
        so we can take out the empty list check. If we're wrong, then our tests will tell us. 
        So, let's try that.
        We can see that it still passes all the tests.
        
###### __refactoring step 2__

    - We can see that it still passes all the tests.
        Another section of code that  stands out is this section here.
        Anytime I see a for loop I tend to think of using  a list/dictionary comprehension, and this looks  
        like a case to remove all these lines of code  and replace them with a list comprehension.
        Let's look at how we could do that. I’ll  create a basic one and print it out,  
        calling the function with the values [2, 1, 4].
        If I run the file and we see [2, 1, 4] printed  out. Now, we don’t need the values.   
        Looking at our code, we add 1 to the variable evens  each time we get an even number in the list.
        Let’s replace the value with  1 for each item in the list.  
        To do that, we replace the  first n with the number 1.
        If we run our file, we get [1, 1, 1].
        That’s better and more useful, but our code  uses an if statement to ignore odd numbers,  
        so let’s add that to our  comprehension. That gives us:
        1 for n in numbers if n % 2 == 0
        If we run the code again, we get: [1,1] 
        And finally, we can wrap the list comprehension  in the sum() method to get a total.
        When we run the code again we get 2.
        That works great, so we can  assign this to our evens variable  
        and replace all those lines of code.

###### __refactoring step 3__
    - Another section I see we can  easily refactor is this section.
        This looks like it should easily be  converted to a single line conditional expression
        which would take the format: True if condition else False.
        So let's try doing that.
        For the condition I see I need two checks.  
        First, we check if evens is not 0, so  let’s use a truthy check to do that.
        Second, evens % 2 == 0, so lets add that as well.
        And there we go: return True if evens  not 0 and evens % 2 == 0 else False.
        Let’s see what happens if we run the tests again. And they all pass, great!

### __End of stage 3 - refactoring__

So we have refactored our code and all our  tests pass. That means we’ve covered all  
phases of the red-green-refactor cycle. In this and the previous videos we have  
learned how to build out our code using  unit tests and how to refactor our code.
Now that you are familiar with how  to build tests, we’re going to have  
a look in our next unit at testing class properties and methods. See you there!

# __OUR STUDENT CLASS__
# __Stage 4 - Our Student Class__
In the previous lessons, you learned  about the Unittest framework,  
making assertions, catching errors and  revised the Test-Driven Development process. 
In this video, I’ll introduce the Student class which we’ll be using for the remainder of this module.
I promised that things would get exciting and  this is where it begins. So far, we’ve used a  
pure Test-Driven Development process for testing  purposes.

    - We’ll take a slightly different approach  
        here by creating a Student class with some basic  functionality before our tests. We’ll then add  
        functionality using Test-Driven Development once  we’re familiar with creating tests for methods.
        Our Student class will have all the basic  functionality one might expect to see when  
        needing to handle multiple students with different start and end dates. I say basic functionality  
        as there is a lot that can be added to make this usable in a real-world scenario.
        For now, it will work quite nicely for our tests. Let’s  start by creating a file called student.py.   

#### __Student.py__
    - Once created, I’ll go ahead and define a class called  Student and add a docstring stating what it’s for.
        To allow us to define start and end  dates, we’ll use two methods from the  
        datetime module called date and timedelta  which I’ll import at the top of the file.
        Next, we can define our init method. It will have  three parameters: self, first_name and last_name.  
        Inside the init method, we can set  self._first_name to be equal to first_name  
        and self._last_name equal to last_name.
        As we want these to be read-only  fields, we can prepend the first_name  
        and last_name properties with an underscore so  other developers know how it should be used.
        We’ll also go ahead and define a start_date  which will be set using the date.today() method.  
        When an instance of our Student class is created,  the start_date value is set using the time at  
        the moment of the instance’s creation. In our  fictional school, students will enroll for a year,  
        so we can define end_date and set it equal  to date.today() plus a timedelta of 365 days.  
        This doesn’t allow for leap years, so if you want  to improve this class at the end of the module,  
        this might be something worth looking into.
        Finally, we’ll add a field called naughty_list  which is set to False initially. This is of course  
        so we can let Santa know if a student misbehaves  and redirect their presents to ourselves.
        With the init method defined, we can  go ahead and create a read-only method  
        to get more detailed information about a  student, such as the student’s full name.  
        Let’s add a method called full_name,  add self as a parameter and return an  
        f-string consisting of self._first_name  and self._last_name separated by a space.  
        Since this is a method to get data only, I’ll add  the @property decorator to our full_name method.
        We will add more methods to our  Student class in later videos,  
        but we can see that our Student class can  be extended to add a lot more functionality  
        and I encourage you to try that at the end  of the module to cement your knowledge of  
        testing in Python while creating  truly practical and usable code.

### __end of stage 4__
In this lesson, we created a student.py file  with a Student class which will form the  
base of our tests. It has properties, sets values  automatically on creating an instance of the class  
and has a method to return a student’s full name. In the next video, we’ll write the first test  
for our Student class to ensure it provides  the functionality we expect. See you there!

# __Stage 5 - OUR STUDENT CLASS - Testing methods and properties__
    - In the previous lesson, we created a basic Student  class with properties and a full_name method. 
        In this lesson, we’ll look at testing the  full_name method of our Student class.
        Now that our Student class is in place,  how would we go about testing it?  
        If you thought that we would need to  create an instance of the class first...
        Well done! Before we can do that, however, we  need to do our basic setup of our test file.  
        Using the knowledge you’ve gained so far, pause  the video and create a file using the naming  
        convention mentioned in an earlier lesson while  also setting up an empty class for our tests.

#### __test_student.py__
    - At this point, you should have  a file called test_student.py,  
        and our required imports including Unittest and our  Student class. A class named TestStudent that  
        inherits from unittest.TestCase is also required.  Though it isn’t required, I’ll add the same if  
        statement we used before so we can run the file  without having to specify the Unittest module.
        With that now in place, we can start  creating our first test and we’ll do so  
        for the full_name method. I’ll name the method  test_full_name and pass in a reference to self.
        As mentioned earlier, we need to  create an instance of the Student class  
        in order to test it. I’ll name  the instance student and make  
        sure to pass in the first_name and last_name  arguments of ‘John’ and ‘Doe’ respectively.
        We can now use an assertEqual on the  student instance to see whether calling  
        the full_name method on it returns  the expected value.   
        In our case, the first_name and last_name  properties separated by a space.
        If we now run our test, we can see that it  passes. Great! 
        
That’s our first test done,so we’re well on our way towards extending  the scope of our tests and Student class.
In this video, we wrote the first test for our  Student class. We created an instance of the  
class and asserted that the full_name method  returns the correctly formatted student name. 
In the next video, we’ll start  employing Test-Driven Development  
for our Student class. We’ll create a new test  
to change the naughty list property to true  before creating the method to be tested. See you there!  



























