'''Our predict_weather function should output a message indicating whether a sunny or cloudy day lies ahead. However, the output is the same every time the function is invoked. Why? Fix the code so that it behaves as expected.

Copy Code
import random

def predict_weather():
    sunshine = random.choice(['True', 'False'])

    if sunshine:
        print("Today's weather will be sunny!")
    else:
        print("Today's weather will be cloudy!")
'''

import random

def predict_weather():
    weather = ['sunny', 'cloudy', 'rainy']
    selected_weather = random.choice(weather)

    if selected_weather == 'sunny':
        return("Today's weather will be sunny!")

    else:
        return("Today's weather will not be sunny!")
    
print (predict_weather())

# the random.choice will be always True, so we need to change the options to something that creates a 50% possibilities, like sunny and cloudy. 

# Launch school is easier 
# In order for the function to behave as expected, we should assign sunshine to the boolean True or False instead of the string 'True' or 'False'.

'''
import random

def predict_weather():
    sunshine = random.choice([True, False])

    if sunshine:
        print("Today's weather will be sunny!")
    else:
        print("Today's weather will be cloudy!")
'''

#additional is always better to use return instead of print inside the functions, to avoid printing None as part of the output 
# The function itself returns None because Python functions always return something, and if there is no return statement, the function implicitly returns None.
