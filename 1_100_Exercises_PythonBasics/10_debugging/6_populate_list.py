'''You want to add the numbers from 1 to 5 to a list, but the code below is not producing the expected result. How can you fix it?

Copy Code
numbers = []

for i in range(5):
    numbers.append(i)

print(numbers)'''

numbers = []

for i in range(1, 6):
    numbers.append(i)

print(numbers)

# changing the range, if we don't specify a range always starts with the value '0', the last value of the range is never included in the output, therefore to get the output [1, 2, 3, 4, 5] we need to change the range to range(1, 6)