'''Using the following code, compare the value of name with the string 'RoGeR' while ignoring the case of both strings. Print true if the values are the same; print false if they aren't. Next, perform a case-insensitive comparison between the value of name and the string 'DAVE'.

name = 'Roger'
'''

name_1 = 'RoGeR'
name_2 = 'Roger'
print (name_1.casefold() == name_2.casefold())

name_3 = 'DAVE'
print (name_2.casefold() == name_3.casefold())

# to compare strings use str.casefold() instead of str.lower(), it is especially designed to compare strings case-insensitive in languages where conventional methods may fall. 