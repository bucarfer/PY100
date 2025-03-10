# Use the Python documentation for the str class to determine which method can be used to right justify a str object.

'''acces to https://docs.python.org/3/ 
inside there we click on library reference 
once inside we click on strings 
inside strings we search for right justify

str.rjust(width[, fillchar]) 
Return the string right justified in a string of length width. Padding is done using the specified fillchar (default is an ASCII space). The original string is returned if width is less than or equal to len(s).
'''

text = input ('type text to be justified: ')
print (text.rjust(30, '*'))