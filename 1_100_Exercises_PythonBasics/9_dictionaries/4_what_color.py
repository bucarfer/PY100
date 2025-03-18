'''Using the following code, select and print the value 'blue' from the car object:

Copy Code
car = {
    'type':  'sedan',
    'color': 'blue',
    'year':  2003,
}
'''

car = {
    'type':  'sedan',
    'color': 'blue',
    'year':  2003,
}

print (car.get('color')) 
# 'get' is the function to use if we are not sure if the key value exists 

# you can also use brackets and no .get:
# print(car['color'])