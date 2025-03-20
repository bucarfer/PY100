'''You are trying to access a value in a dictionary, but the code is giving you an error. Can you change line 3 so that it prints "Unknown" instead of raising an error?

Copy Code
info = {'name': 'Srdjan', 'age': 38}

print(info['city'])'''

info = {'name': 'Srdjan', 'age': 38}

print(info.get('city', "Unknown"))

# change to the command my_list.get('key', 'other option') using get with a default value prevents the error and provides a fallback value

# alternative solution of L.S. but less pythonic was to first check whether the key is in the dictionary and if it is not, print "Unknown"