'''The following code raises a SyntaxError:
What does a SyntaxError indicate? Try running the above code, then use the resulting error message to fix the error.

speed_limit = 60
current_speed = 80

if current_speed > speed_limit
    print('"People are so bad at driving cars that '
          "computers don\'t have to be that good to be "
          'much better." -- Marc Andreessen')'''

#SyntaxError occurs when Python cannot understand the code due to a structure or grammar error, in this case the colon symbol ':' was missing. correct code:

speed_limit = 60
current_speed = 80

if current_speed > speed_limit:
    print('"People are so bad at driving cars that '
          "computers don\'t have to be that good to be "
          'much better." -- Marc Andreessen')