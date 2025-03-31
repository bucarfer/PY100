# Given a list of student names and a list of corresponding 
# grades, write some code to create a dictionary with the 
# names as keys and their associated grades as the values.

students = ["Alice", "Bob", "Charlie"]
scores = [97, 92, 78]

# Your code here

## Bonus Questions ##
# 1. What happens if the two lists have different lengths? 
#    How can you handle this case in your code?
# 2. How could you modify the dictionary later if a 
#    student's grade changes? What method would you use?
# 3. Which do you think is a better structure for managing 
#    students and their grades, two lists or a dictionary?

# Main problem:

students = ["Alice", "Bob", "Charlie"]
scores = [97, 92, 78]

grades = {}
set_number = range(0,len(students))

for set in set_number:
    grades[students[set]] = scores[set]

print (grades)

# Bonus 1.
# We could use zip first, this function will stop when either of the two lists stops, ones we have both list we can create the dictionary.

students = ["Alice", "Bob", "Charlie"]
scores = [97, 92, 78]

zipped_dict = dict(zip(students,scores))
print(zipped_dict)

# Bonus 2
# I would use the "update key-value" built-in function 

grades ['Bob'] = 95 
print (grades)

# Bonus 3
# A dictionary because we can always add new pairs or modify the existing one by key-value 