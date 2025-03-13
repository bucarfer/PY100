'''Without running the following code, determine what it will print:
'''

def multiples_of_three():
    divisor = 1

    for dividend in range(3, 31, 3):
        print(f'{dividend} / {divisor} = 3')
        divisor += 1

multiples_of_three () # parenthesis added to invoke de function 

# no output since the function 'multiples_of_three' is never invoked, in order to invoke the function we need to append parentheses to the function in line 11. After that the ouput is 
'''
3 / 1 = 3
6 / 2 = 3
9 / 3 = 3
12 / 4 = 3
15 / 5 = 3
18 / 6 = 3
21 / 7 = 3
24 / 8 = 3
27 / 9 = 3
30 / 10 = 3
'''