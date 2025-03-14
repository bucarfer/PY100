'''What will the following code do and why? Don't run it until you have tried to answer.

a = 1

def my_function():
    a = 2

my_function()
print(a)'''

# it will print the global variable 'a' with the value 1. The local variable 'a' with the value 2 is only initiated and assigned the value 2 inside the function (locally)

a = 1

def my_function():
    a = 2

my_function()
print(a)