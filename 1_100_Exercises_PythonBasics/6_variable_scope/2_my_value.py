'''What will the following code do and why? Don't run it until you have tried to answer.

x = 10

def my_function():
    x = x + 5
    print(x)

my_function()
'''

# it gives the following error 
# UnboundLocalError: cannot access local variable 'x' where it is not associated with a value. In the function we are trying to reassign the value of X inside the function. However to do that we need to use the 'global' keyword.

x = 10

def my_function():
    global x
    x = x + 5
    print(x)

my_function()