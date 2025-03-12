'''Take your code from the previous Check the Weather exercise and rewrite it as a match-case statement. Feel free to add more cases besides 'sunny' and 'rainy'.'''

import random
weather = random.choice (['sunny', 'rainy', 'windy', 'snowy'])

match weather:
    case 'sunny':
        print (f"Its a beautiful day! The weather is {weather}")
    case 'rainy':
        print (f"Grab your umbrella. The weather is {weather}")
    case _:
        print (f"Let's stay inside. The weather is {weather}")


    