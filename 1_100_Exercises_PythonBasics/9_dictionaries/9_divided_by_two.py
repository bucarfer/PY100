'''Use a for loop to iterate over the numbers dictionary and return a list containing each number divided by 2 as an integer. The result should be truncated to an integer. Assign the returned list to a variable named half_numbers and print its value using print.

Copy Code
numbers = {
    'high':   100,
    'medium': 50,
    'low':    25,
}
Expected OutputCopy Code
[50, 25, 12]'''

numbers = {
    'high':   100,
    'medium': 50,
    'low':    25,
}

half_numbers = []

for value in numbers.values():
    half_numbers.append(value//2)

print (half_numbers)

# this one I could not do it without Launch school solution
# the "//"" operator performs integer division, which yields the correct types, we cannot use the "/" operator