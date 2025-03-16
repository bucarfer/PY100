'''We are given the following list of energy sources.

energy = ['fossil', 'solar', 'wind', 'tidal', 'fusion']
Write some code to remove 'fossil' from the list, then add 'geothermal' to the end of the list.'''

def add_and_delete (lst):
    lst.remove('fossil')
    lst.append('geothermal')
    return lst

energy = ['fossil', 'solar', 'wind', 'tidal', 'fusion']
print(add_and_delete (energy))