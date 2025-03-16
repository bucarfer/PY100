'''The destinations list contains a list of travel destinations.

destinations = ['Prague', 'London', 'Sydney', 'Belfast',
                'Rome', 'Aruba', 'Paris', 'Bora Bora',
                'Barcelona', 'Rio de Janeiro', 'Marrakesh',
                'New York City']
Write a function that, without using the built-in in operator, checks whether a specific destination is included within destinations. For example: When checking whether 'Barcelona' is contained in destinations, the expected output is True, whereas the expected output for 'Nashville' is False.

'''
destinations = ['Prague', 'London', 'Sydney', 'Belfast',
                'Rome', 'Aruba', 'Paris', 'Bora Bora',
                'Barcelona', 'Rio de Janeiro', 'Marrakesh',
                'New York City']

def contains (item, lst):
    if lst.count(item) > 0:
        print (True)
    else:
        print (False)

contains('Barcelona', destinations)  # True
contains('Nashville', destinations)  # False

# Launch school solution uses the word "in" without using the built-in function with "in"

'''def contains(element, lst):
    for item in lst:
        if item == element:
            return True

    return False'''

# this approach iterates over all the values of the list and only returns true if one of them has the same value as the first parameter 'element'

# alternative launch school option using while: 

'''def contains(element, lst):
    index = 0
    while index < len(lst):
        if lst[index] == element:
            return True

        index += 1

    return False'''