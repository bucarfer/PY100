'''Using the official Python documentation, can you determine how to check whether a string contains a specific substring?'''

# we can use find() and in(), the find() method should be used only if you need to know the location of sub. To check if sub is a substring or not, just use 'in' operator

print ('Py' in 'Python') #True
print ('rst' in 'restaurant') #False

#example with find()
text = 'python is hard to learn'
index = text.find('hard')

if index != -1:
    print (f'substring found at index {index}')

else:
    print ('substring not found')