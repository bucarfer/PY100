'''What will the following code do and why? Don't run it until you have tried to answer.

a = 1

def my_function():
    global a
    a = 2

my_function()
print(a)'''

# te code will print the global 'a' value of '2', that was reassigned inside the function thanks to the global keyword. 

a = 1

def my_function():
    global a
    a = 2

my_function()
print(a)