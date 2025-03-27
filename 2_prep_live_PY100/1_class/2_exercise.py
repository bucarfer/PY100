# What is the output when you run this code?

def greet(name):
    return 'Hello, ' + name + '!'


greet('Alice') 
print(greet('Bob'))
print(greet(''))

# in the first line we dont capture the return value 
# Hello, Bob !

'''
Bonus questions
5.1. What is the difference between using return and print in a function?

Using return doesn’t print out the output of the function when we run the function, but stores the result, using “print” prints out the output but doesn’t store the result. 

5.2 What would happen if we called greet() without any arguments?
# my answer, if we print the function the return will be --> hello, !
# correct answer, it will raise an error, missing 1 required positional argument 

5.3 Can you modify the function to handle the case when no name is provided?
'''
# option A:
def greet(name=""):
    if not name:
        return "Hello, stranger!"
    else:
        return 'Hello, ' + name + '!'

#simplified version:

def greet(name="no input received"):
        return 'Hello, ' + name + '!'

print(greet())