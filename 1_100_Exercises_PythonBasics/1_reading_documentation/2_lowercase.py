# Determine whether Python has a method to lowercase a string, for example converting 'Aloha, World!' into 'aloha, world!.

# the command to convert text to lowercase is string.lower()

text = input('copy text to convert to lowercase: ')
text = text.strip()
text = ' '.join(text.split())
print('Lowercase version:', text.lower())
