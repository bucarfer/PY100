'''What will the following code do and why? Don't run it until you have tried to answer.

b = [1, 2, 3]

def my_function():
    b[0] = 10

my_function()
print(b)'''

# This is a tricky case, list are mutable and therefore we can change the contents of the list (not reassignment) without the need of changing the global value of the variable 'b'. 
# The code will print [10, 2, 3] because my_function changes the first content of the of the global list from 1 to 10 (index reassignment, mutating the list). 
# reassignment is different to index reassignment.