'''Write a function that returns the first element of a list provided as an argument. For example:

print(first(['Earth', 'Moon', 'Mars']))  # Earth
Be sure to handle the case where the input list is empty.
'''

def first (lst): #never use list as a variable to dont override list 
    if lst:      #truthy value, empty list is falsy 
        return lst[0]

    else:
        return None

print(first(['Earth', 'Moon', 'Mars']))
print(first([]))