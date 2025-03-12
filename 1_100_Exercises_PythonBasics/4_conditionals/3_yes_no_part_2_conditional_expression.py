'''Rewrite your code from the previous exercise to use a ternary expression.

if random_number == 1: 
    print ('Yes!')
else:
    print ('No')
    '''

import random
random_number = random.randint(0, 1)

print ('Yes!' if random_number else 'No') # random_number == True, random_number == 1

# what is ternary expression? The oficial name of ternary expression is conditional expression, the syntatical structure of the ternary expression is: 
# expression1 if condition else expression2