# What will be the output of this code? Why doesn’t this code change the 
# value of `my_element`?

my_element = { 'language': 'JavaScript' }
my_list = [my_element]
'''my_list[0] = { 'language': 'Python' }
print(my_element)'''

# { 'language': 'JavaScript' } because line 5 is assigning to the list a new dictionary.

## Bonus Questions ##
# 1. How could we update this code to get an updated dictionary output?
# opt 1 -> my_element['language'] = 'Python'
# opt 2
my_list[0]['language'] = 'Python'
print(my_element)

# 2. How many dictionaries exist in the original snippet? How many exist 
#    in your solution to bonus question 1?
# in the original snippet we had 2 dictionaries and with the new change only one dictionary 

# 3. If indexed assignment is mutating, why wasn’t `JavaScript` 
#    changed to `Python`?
# because inside the list index we had a dictionary and to modify a dictionary we need the command used in the first bonus answer, if not Python creates a new dictionary instead of modifying the original one 
