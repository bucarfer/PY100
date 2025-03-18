'''Which Collection?
Rewrite car as a list of lists in which each nested list contains two elements that represent the corresponding key/value pairs.

Copy Code
car = {
    'type':  'sedan',
    'color': 'blue',
    'year':  2003,
}
'''

car = [
    ['type', 'sedan'],
    ['color', 'blue'],
    ['year', 2003],
]

print(car[2][1]) # 2003

# dictionaries as of python 3.6 maintain order now, but lists still the preferred option for maintaining order 