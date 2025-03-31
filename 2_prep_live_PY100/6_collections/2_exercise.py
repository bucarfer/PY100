# What happens when we run this code? Why?

'''numbers = [1, 2, 3]
numbers.append(4, 5)
print(numbers)'''

## Bonus Questions ##
# 1. We wanted to create the result list of `[1, 2, 3, 4, 5]`.
#    What are two distinct ways we could fix this code to 
#    achieve this result?
# 2. Based on the intent of this original code, can you 
#    tell me if we should be mutating our list? Why or why 
#    not?
# 3. What happens if we append a list with '4' and '5' instead.


# Main exercise:
# It gives us an error because append only works with one new argument

numbers = [1, 2, 3]
numbers.append(4)
numbers.append(5)
print(numbers)

# Bonus 1.
# using append twice or using extend, remember that extend needs one list argument, if not it will also raise an error

numbers = [1, 2, 3]
numbers.extend([4, 5])
print(numbers)

# Bonus 2.
# Because they didn't try to change the variable name, the intent of the code must be mutation. To mutate the list we can use list.append() or list.extend([]).
# If we didn't have to keep the original list we could have reassign to a new list -> new_numbers = [1, 2, 3, 4, 5]

# Bonus 3.

numbers = [1, 2, 3]
numbers.append([4, 5])
print(numbers) # [1, 2, 3, [4, 5]]

# It appends the list within the other list, creating a nested list.