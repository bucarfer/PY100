'''In the following code snippet, find all violations of the PEP8 style guide. Rewrite it so that it conforms with the guide.

iceCreamDensity=10

while iceCreamDensity>0 :
    print('Drip...')
    iceCreamDensity-=1

print('The ice cream melted.')'''

icecream_density = 10

while icecream_density > 0:
    print('Drip...')
    icecream_density -= 1

print('The ice cream melted.')

'''Here are the PEP8 guidelines that were not followed in the original code snippet:

Variable Naming: Variables should be in snake_case instead of camelCase.
Spacing: There shouldn't be a space before the colon in the while loop.
Missing Spaces: There should be a single space on both sides of the =, >, and -= operators.'''