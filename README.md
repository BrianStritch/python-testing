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

### __end of stage 5__        
That’s our first test done,so we’re well on our way towards extending  the scope of our tests and Student class.
In this video, we wrote the first test for our  Student class. We created an instance of the  
class and asserted that the full_name method  returns the correctly formatted student name. 
In the next video, we’ll start  employing Test-Driven Development  
for our Student class. We’ll create a new test  
to change the naughty list property to true  before creating the method to be tested. See you there!  

# __STAGE 6 - Building a method using TDD - creating the first test__
#### __test_student.py - santa naughty list__
    - In the previous lesson, you created your first test for our Student class where you instantiated
        it and called the full_name method on it to assert whether it returned the first_name
        and last_name property values separated by a space.
        In this lesson, we’ll start using Test-Driven Development and create a test for a function
        called alert_santa that  will change the naughty_list property to True.
        We don’t have the method we want to test yet, but we do know what we want it to do.
        If a student misbehaves for some inexplicable reason, we want to alert Santa by adding the student to his naughty list.
        When the class is instantiated, the naughty_list  property is set to False.

#### __naughty list__
    - So, we know that the method we want to test will  set the value of the naughty_list property to  
        True and this makes it easily testable. Since  we want to alert Santa, we’ll make a decision  
        now to call that method alert_santa so we can  use it in our tests before it’s been created.
        Following the naming convention for  test methods, I’ll go ahead and create  
        a method called test_alert_santa  and pass in a reference to ‘self’.
        As before, we need to create an instance  of our student class and call it student. 
        We’ve been using assertEqual methods up till now,  
        but we’ll use a different assert  for this test called assertTrue.
        The reason being that we know that  we want the alert_santa method to set  
        the value of the naughty_list  property to True when called.
        With our student instance created,  let’s call the alert_santa method on it. 
        Now, we can use self.assertTrue to test  whether student.naughty_list is True. 
        Note that we don’t pass a second  argument to assertTrue as it’s not  
        comparing two values but simply checking  whether an expression or value is True.
        What do you expect will happen if we run our tests  now? Since our alert_santa method doesn’t exist in  
        the Student class yet, we expect it to fail with  an error. Let’s run the tests now and check that.
        And, as expected, it fails with an  AttributeError. This completes the  
        “red” stage of our red-green-refactor methodology.

### __End of stage 6__
In this lesson, we started following  the TDD principle and created a test  
called test_alert_santa that will test the  behaviour of a method called alert_santa  
that we still need to create in the Student class. 
In the next lesson, we’ll create the  alert_santa method in the Student class  
and run our tests again to complete the “green”  part of red-green-refactor. See you there!

# __STAGE 7 - Building a method using TDD - creating the code__
In the previous video, we started  applying Test-Driven Development  
by creating a test called test_alert_santa  that will test the functionality of a method  
called alert_santa that hasn’t been created  yet. We also watched this test fail as expected. 
In this video, we’ll create  the alert_santa method,  
rerun our tests and confirm that they’re passing.
As seen in the previous video, we had a pretty  good idea of what our alert_santa method needs to look like.
It isn’t a read-only method  and will modify the naughty_list property  
instead of returning a value. With  this in mind we can create our method.
Let’s create it below the full_name method.  

#### __CREATING THE ALERT_SANTA FUNCTION__
    - We’ll call it alert_santa to mirror the name  used in our test_alert_santa method and pass in  
        a reference to self. I’ll add self.naughty_list  equals True to update the property value.
        With this in place, let’s run our  tests again and see if they pass.  
        And we can see that both of them do.  Fantastic! We’ve now completed the  
        “green” part of our red-green-refactor  process for the alert_santa function.

#### __task set by instructor__
    - While we’re at it, let’s add another test and  function. I’ll let you take the reins for this one  
        and we can look at my implementation afterwards.  What we want is a read-only method that will  
        return a student’s email address. It will take  the form _first_name dot _last_name@email.com.  
        For simplicity’s sake, all email  addresses will end in email.com.  
        You can create the test for this first, followed  by the actual method itself in the student class.  
        If you’re uncertain how to proceed, use the  test_full_name and full_name methods as reference.  
        Pause the video now and work away on that  and unpause to compare your code to mine.

    - Welcome back. I’ll implement it  quickly so you can reference my code.
        First, I’ll create a new test method called  test_email with a reference to self.
        Inside it, I’ll create an instance of the Student class using  the first and last name properties as before.  
        Next, I’ll code our assertEqual and compare the  output of student.email to the expected output.  
        Email addresses use lowercase letters, so  I’ll make sure to add a second argument  
        to the assert with the first and last  names values adjusted appropriately.  
        To achieve this output, our email  method will need to convert the first  
        and last name properties to lowercase, so we’ll  make sure to do that when the test is done.
        Our test is looking good, so I’ll  go ahead and add our email method  
        to the Student class. As it’s a read-only method,  
        I’ll add the @property decorator and call  the method email with a reference to self.  
        We just need to return a string that includes the  _first_name and _last_name properties separated  
        by a dot, followed by email.com. As mentioned  earlier, the _first_name and _last_name values  
        need to be converted to lowercase, so I’ll make  sure to do that using the lower() string method.
        With that in place, I’ll run our tests again  to confirm that they pass, which they do!

### __End of stage 7__
In this lesson, we created the alert_santa  method in our Student class and created another  
test for our email method which we then created  afterwards. We also confirmed that our tests are  
passing with these new additions to our code. In the next lesson, we’ll take a look at the  
lifecycle of a test and how we can refactor our  tests based on what we’ll learn. See you there!


# __STAGE 8 - The lifecycle of a test__
# __***** setUp / tearDown *****  setUpClass / tearDownClass *******__
- In the previous lessons, we added the test_alert_santa and test_email methods to our  
testing file, as well as creating the alert_santa and email functions in our Student class. 
In this video, we’ll look at the  lifecycle of a test - more specifically,  
how and when the tests are run and how instances are created and destroyed when running our tests.

- At the moment, we’ve got quite a bit  of repetition in our test functions. In every test, we’re manually creating the same  student instance on which to perform our tests. This violates the DRY, or Don’t  Repeat Yourself, principle.  
Our TestStudent class contains  only a few test methods, but can you imagine how much code repetition  we’d have if we had many more tests to run? Luckily for us, Unittest gives us two methods  that will be run at the beginning and end of each test method. They are called setUp and  TearDown respectively, are optional and are used to set up and teardown or destroy a testing  environment for each test method. It’s important to note that these methods are defined using camel  case instead of the conventional snake case which is used in Python. This is most likely due to it  having been carried over from older legacy code. It’s important to declare them using  camel case or they won’t run at all.

#### __Back to test_student.py__
    - Since the setUp method runs before each test  method, it would save us code repetition if we  
        could define our student instance there so it can  be available in each test method when it’s run.
        Let’s go ahead and create the setUp method  at the beginning of our TestStudent class  
        and add a reference to “self”. Next, I’ll create  a student instance as an instance variable,  
        so it needs to be prepended with the “self”  keyword. Just so we can see when the setUp  
        method is run, I’ll add a print statement  that’ll print “setUp” to the terminal.
        Since student is now an instance variable,  we’ll need to go and change every reference  
        to self.student. Now that the student instance  will be created in the setUp method at the start  
        of each test method, we can remove the student  instantiations in each of them. I’ll also add a  
        print statement to each test method which will  print the method’s name to the terminal.   
        This will allow us to see when our test methods are  run relative to the setUp and tearDown methods.
        We won’t be using any functionality that  requires the use of the tearDown method, but you may be wondering what it’s for.
        Whereas the setUp method can be used to  create temporary files and folders or set up  
        a database connection during tests, the tearDown  method would be used to remove temporary files  
        or folders or close a connection to a database. As  we don’t need any of that functionality, adding a  
        simple statement to print “tearDown” will allow  us to see when it is called behind the scenes.
        Everything is now in place to test whether our setup works. Let's see what happens when we run our tests.
        Just as expected. For each test, we can see in  order the following printed in the terminal:  
        setUp, followed by the name of  the test and finally, tearDown.  
        This shows that the setUp method is run before  each test, while the tearDown method is run after.  
        The fact that all our tests still pass  indicates that our student instance was  
        indeed created successfully and that  it was accessible within each test.  
        It is interesting to note that the tests  don’t run in the order we defined them.  
        What is important, however,  is that they do all get run.
        Now consider we want to run code once at the  beginning of our tests. We may want to do this to  
        populate a test database with data, for example.  We can’t use the setUp method as that gets called  
        at the beginning of each test method. Fortunately,  Unittest provides another method we can use for  
        this particular use case called setUpClass.  We can also use the tearDownClass method  
        to destroy a test database, for instance, and this  method will be run once at the end of our tests.
        As we don’t have a particular use for  it in our test, I’ll simply show you  
        how to set up these methods and add print  statements so we can see when they are run.
        At the top of our test_student file, I’ll go  ahead and add setUpClass with a parameter of ‘cls’  
        instead of ‘self’. I do this as setUpClass is  a class method that affects the class itself  
        instead of only an instance of the  class as the ‘self’ parameter would.  
        Let’s add a print statement inside our method that  will print “setUpClass” to the terminal when run.  
        There is one more thing we need to  add to make this a class method,  
        and that is the @classmethod  decorator. Just to reiterate,  
        adding the @classmethod decorator to a method  and passing ‘cls’ as a method parameter  
        will make it a class method which acts on the  class instead of an instance of the class.
        I’ll do the same thing for  the tearDownClass method,  
        but print “tearDownClass”  inside the method instead.  
        Let’s not forget to add  the @classmethod decorator.
        We expect the setUpClass and tearDownClass  methods to run once at the beginning and end  
        of our tests instead of before and after each  test method. With our print statements added,  
        we should be able to verify that in the terminal,  so let’s go ahead and run our tests again.
        And we can see “setUpClass” printed  once at the beginning of our tests  
        and “tearDownClass” at the end as expected.  
        These Unittest methods are very powerful and  will be of great use in your future projects.
        Knowing what you want to set up and when  to do so will allow you to utilise the  
        lifecycle of a test to your advantage.  

### __End of Stage 8__
In this lesson , you learned about the lifecycle of a test, including the setUpClass  and tearDownClass methods that are run once at the beginning and end of our tests, as  well as the setUp and tearDown methods that are run before and after each test method. For our  tests, you used the setUp method to automatically create a student instance, allowing you to  refactor the code and make it more legible.

In the next lesson, you’ll take  charge and create a new test and method to satisfy the challenge  requirements. See you there!

# __Stage 9 - CODE ALONG CHALLENGE__
In the previous video, you learned  about the lifecycle of a test and  
how to use it to refactor and optimise your code. 
In this video, you’ll take charge and  use the Test-Driven Development process  
to create a new test and function to extend  the functionality of our Student class.
There are still properties in our Student class  that aren’t really doing anything at the moment,  
and these are start_date and end_date. Until  time travel is invented, there shouldn’t be a  
reason to change a student’s start date. It’s  set automatically when we create an instance  
of the Student class, and as long as our time  is set correctly, we won’t have to modify this value again.
The end date is another matter  though. Due to unforeseen circumstances,  
none of which of course relate to time  mismanagement by a student (cough cough),
a short extension could be offered to help them finish the  course. This is what you’re going to implement.
The requirements are as follows:

#### __list of requirements__
    - Create a test called test_apply_extension  that will assert whether a method called  
        apply_extension updates a student’s  end_date by adding a number of days to it.  
        The number of days needs to be passed  into apply_extension as an argument.
        Then create a method in the Student  class called apply_extension that will  
        have a parameter called days and  will update a student’s end_date  
        by adding the argument given as  days to their original end_date.
        Think this through before you start  coding and look at the questions you  
        need to ask yourself at the bottom of this slide.
        Having a look at the timedelta  documentation is also recommended.  
        Pause the video now and try to implement that  before coming back to see how I go about doing it.

#### __answer to complete challenge__
    - create a new test method called test_apply_extension
    - inside test_apply_extension, store the current end date for our test student instance in a variable called old_end_date
    - call a method named apply_extension that will take a number of days as an arguement on the student instance to update the end_date
    - assert whether the instance's end date equals the old end date plus the days arguement that was passed in using timedelta
    - run the tests to confirm that the new method is failing
    - in the student class, create a new method  called apply_extension that has a parameter called days
    - use the timedelta method from timeline to update the end_date property
    - run the tests to confirm they are working

    The method below is also great!  But keep in mind that  it will
        only be correct if a student has received 1 extenstion.  If 
        they receive a second - it would return false
        
        self.student.apply_extension(5)
        self.assertEqual(self.student.end_date, self.student._start_date + timedelta(days=370))

### __End of stage 9__
In this lesson, you took charge and created a  test and method to extend a student’s end date. 
In the next lesson, I’ll introduce  you to a concept call mocking  
so we can test functionality which may fail  for reasons beyond our control. See you there!

# __Stage 10 MOCKING__

In the previous video, you created a test  method called test_apply_extension and the  
apply_extension method it tests. You followed  the Test-Driven Development process to do so,  
and confirmed that all tests were passing. In this video, we’ll have an introduction to  
mocking and how it allows us to test functionality  that could fail due to factors beyond our control.
Up till now, we’ve written some comprehensive  tests for our Student class.   
They're comprehensive in the sense that they shouldn’t  fail due to external factors.  
But what would happen if our class needed to make a call to an external API? What if the external server is down? 
How can we test for something that  we as developers can’t control?
Our methods may have complex  logic with try except blocks  
or if statements that may be hard to satisfy  and it can be hard for developers to test  
the complete flow of logic through methods as  they can’t cause a dependency to fail at will.
This is where mocking comes into play. The purpose  of mocking is to focus on the behaviour of the  
code being tested - not the state or behaviour  of external dependencies.
In essence, we mock, or imitate the behaviour of external factors to confirm that our methods work as intended.
In the next video, we’ll create a new method  in our Student class that will make a call to a  
fictional API to get a student’s course schedule.  We’ll then create a test for it and mock the  
request being successful and failing to ensure  our method behaves as expected. See you there!
















