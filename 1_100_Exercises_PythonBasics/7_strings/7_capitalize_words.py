'''Write code that capitalizes the words in the string 'launch school tech & talk', so that you get the string 'Launch School Tech & Talk'.
'''

string = 'launch school tech & talk'
capitalize_string = string.title()
print (capitalize_string)

'''
Launch school alternative:
def capitalize_words(string):
    words = string.split(' ')
    capitalize_words = []

    for word in words:
        capitalize_words.append(word.capitalize())
    
    return ' '.join(capitalize_words)

string = 'launch school tech & talk'
print (capitalize_words(string))
'''