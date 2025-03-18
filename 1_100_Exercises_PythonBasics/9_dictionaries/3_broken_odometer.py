'''Using the following code, delete the 'mileage' key and its associated value from car.

Copy Code
car = {
    'type':    'sedan',
    'color':   'blue',
    'mileage': 80_000,
    'year':    2003,
}'''

car = {
    'type':    'sedan',
    'color':   'blue',
    'mileage': 80_000,
    'year':    2003,
}

car.pop('mileage')
print(car)

# my_dict.pop('key') returns the deleted value apart from deleting it from the list, the simplest solution in this case would be: 
# del my_dict['key']