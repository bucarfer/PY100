'''What will the following code do and why? Don't run it until you have tried to answer.

a = 1

def my_function():
    print(a)
    a = 2

my_function()'''

# it will give a localError because we are trying to reassign the global variable 'a' within the function after invoking the global variable with the print command. The error raise is: UnboundLocalError: local variable 'a' referenced before assignment. In order to fix it we can first assigned the local valuable a = 2 and after invoke the command print that will take the local variable.

a = 1

def my_function():
    a = 2
    print(a)

my_function()