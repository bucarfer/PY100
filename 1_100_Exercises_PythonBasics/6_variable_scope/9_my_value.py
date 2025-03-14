'''What will the following code do and why? Don't run it until you have tried to answer.

a = 7

def my_function(b):
    b += 10

my_function(a)
print(a)'''

# In python integer are immutable. When the function scope is called using a as the variable, the local variable of b is set to have the same vale as a, which is 7, during the execution the function creates a new integer assigned to the local variable 'b' with the value of 17. However the original variable a remains unaffected and retains its value of 7. 

a = 7

def my_function(b):
    b += 10

my_function(a)
print(a)