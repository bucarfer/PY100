pets = {
   'cat' : 'Meows',
   'dog' : 'Barks',
   'bird' : 'Tweets',
}

key = input ('write an animal:').strip().lower()
value = pets.get (key, 'is an unregistered animal')

print (f'the {key} {value}')
