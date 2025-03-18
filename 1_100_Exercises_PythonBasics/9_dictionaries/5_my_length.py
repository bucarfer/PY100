'''What's My Length?
Calculate and print the number of key/value pairs in the following dictionary:

Copy Code
car = {
    'type':  'sedan',
    'color': 'blue',
    'year':  2003,
}'''

car = {
    'type':  'sedan',
    'color': 'blue',
    'year':  2003,
}

print(len(car.keys()))

# launch school solution is easier, there is a direct built in function, len(dict) 
# print(len(car))        # 3