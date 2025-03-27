# What is the output when we run this code?

favorite_number = input("What is your favorite number?")
'''y = favorite_number + 5
print(f"Mine is {y}!")'''

# the output is an error because we need to convert the input to an integer before we perform any arithmetic operation 

## Bonus Questions ##
# 1. Once we have an integer, do we need to change it to a string to use it within an f-string? Why or why not? 
# no, there is no need, when we use f_string we can use integers or other non string values, even functions {3+5} between the brackets {}

# 2. How can we fix this code?
# int(favorite_number)

'''y = int(favorite_number) + 5
print(f"Mine is {y}!")'''


# 3. Can you modify the code to print the number associated with concatenating the user's input with 5?
# yes, we can convert 5 into a string 

y = favorite_number + str(5)
print(f"Mine is {y}!")