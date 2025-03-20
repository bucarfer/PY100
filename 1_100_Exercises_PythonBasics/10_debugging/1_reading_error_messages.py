'''You come across the following code. What errors does it raise for the given examples and what exactly do the error messages mean?

Copy Code
def find_first_nonzero_among(numbers):
    for n in numbers:
        if n != 0:
            return n

find_first_nonzero_among(0, 0, 1, 0, 2, 0)
find_first_nonzero_among(1)'''

def find_first_nonzero_among(numbers):
    for n in numbers:
        if n != 0:
            return n

find_first_nonzero_among(0, 0, 1, 0, 2, 0) 
# type error, one positional argument in the function, (numbers), and example with two positionals (numbers, foo) but 6 given
# to fix this line, we change it to one single parameter containing a list of numbers -> find_first_nonzero_among([0, 0, 1, 0, 2, 0]) 
find_first_nonzero_among(1)
#type error, integer number is not iterable 
# similar problem, we need to wrap the integer into a list find_first_nonzero_among([1])

'''difficult problem with Launch solution
Solution
This function expects a list of integers to be passed in as the argument. The example function invocations should look like this:

Copy Code
find_first_nonzero_among([0, 0, 1, 0, 2, 0])
find_first_nonzero_among([1])
Discussion
The first function invocation (line 6) raises an TypeError on line 1:

Copy Code
TypeError: find_first_nonzero_among() takes 1 positional argument but 6 were given
The error message tells you that the function find_first_nonzero_among was given 6 arguments but expects only 1

The second function invocation (line 7) receives the correct number of arguments, so no error is raised on line 1. However, as soon as the program tries to evaluate line 2 with the given argument, it raises another TypeError:

Copy Code
TypeError: 'int' object is not iterable
This is because the function parameter numbers is now bound to the provided argument 1, so it tries to evaluate for n in numbers:. Since integers are not iterables, this raises a TypeError.'''

