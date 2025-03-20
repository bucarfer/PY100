'''Magdalena has just adopted a new pet! She wants to add her new dog, Bowser, to the pets dictionary. After doing so, she realizes that her dogs Sparky and Fido have been mistakenly removed. Help Magdalena fix her code so that all three of her dogs' names will be associated with the key 'dog' in the pets dictionary.

Copy Code
pets = { 'cat': 'pepe', 'dog': ['sparky', 'fido'], 'fish': 'oscar' }

pets['dog'] = 'bowser'

print(pets)  # Output: {'cat': 'pepe', 'dog': 'bowser', 'fish': 'oscar'}'''

pets = { 'cat': 'pepe', 'dog': ['sparky', 'fido'], 'fish': 'oscar' }

pets['dog'].append('bowser')

print(pets)  

# since the key 'dog is associated to a list as a value we can use the list.append method to add additional elements at the end of the list