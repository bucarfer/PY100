'''What will the following code do and why? Don't run it until you have tried to answer.

if True:
    my_value = 20

print(my_value)'''

# I answer it wrong. In Python, variables initialized inside an if, match, while, for, with, or try statement can be accessed, therefore the output will be 20.

'''wht do you think it will happen if we run the following code instead?'''

if False:
    my_new_value = 42

print(my_new_value)

# In this case, Python gives us a nameError, while my_new_value is in scope, it hasn't been initialized to a value yet (because it is Falsy), so remains undefined. 