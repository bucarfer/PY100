'''Initialize a variable weather with a string value being 'sunny', 'rainy', or whatever weather condition you choose. Then, write an if statement that prints:

It's a beautiful day! if weather's value is 'sunny'
Grab your umbrella. if weather's value is 'rainy'
Let's stay inside. if weather's value is anything else
Test your code with different values for weather. '''

import random
weather = random.choice (['sunny', 'rainy', 'windy', 'snowy'])

if weather == 'sunny':
    print (f"Its a beautiful day! The weather is {weather}")

elif weather == 'rainy':
    print (f"Grab your umbrella. The weather is {weather}")

else:
    print (f"Let's stay inside. The weather is {weather}")