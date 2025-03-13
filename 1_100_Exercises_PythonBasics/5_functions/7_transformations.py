'''Use Python's string methods on the string 'Captain Ruby' to create a string with the value 'Captain Python'.'''

def transform(str1):
    str2 = str1.replace('Ruby', 'Python')
    return str2

print (transform('Captain Ruby'))

# other launch school options:
# opt 1:
# first_8 = 'Captain Ruby'[:8]
# new_str = first_8 + 'Python'
# print(new_str)      # Captain Python
# 
# opt 2
# all_words = 'Captain Ruby'.split(' ')
# first_word = all_words[0]
# new_str = first_word + ' Python'
# print(new_str)      # Captain Python