'''Write a function that checks whether a string is empty or not. For example:

print(is_empty('mars'))  # False
print(is_empty('  '))    # False
print(is_empty(''))      # True'''

def is_empty(string):
    return len(string) == 0

print(is_empty('mars'))  # False
print(is_empty('  '))    # False
print(is_empty(''))      # True

''' 
ef is_empty(string):
    return string) == ''

A string is empty if it does not contain any characters. The easiest way is to simply check for an empty string, and nearly as easily, you can check the length of the string.

A more Pythonic approach would be to leverage the fact that an empty string is falsy. By returning the negation of the string using the not keyword, we can obtain a solution that looks like this:

Copy Code
def is_empty(s):
    return not s 

'''