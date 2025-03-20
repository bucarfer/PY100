'''When the user inputs 10, we expect the program to print The result is 50!, but that's not the output we see. Why not?

Copy Code
def multiply_by_five(n):
    return n * 5

print("Hello! Which number would you like to multiply by 5?")
number = input()

print(f"The result is {multiply_by_five(number)}!")'''

def multiply_by_five(n):
    return n * 5

print("Hello! Which number would you like to multiply by 5?")
number = int(input())

print(f"The result is {multiply_by_five(number)}!")

# we fix this problem by using the 'int' function to convert the input to an integer before performing the multiplication, input are always strings 