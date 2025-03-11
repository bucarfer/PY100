'''Modify the following code so the loop continues iterating until the user inputs 'yes'.

while True:
    print('Should I stop looping?')
    answer = input() '''

while True:
    print('Should I stop looping?')
    answer = input()
    if answer == 'yes':
        break
    print ('Incorrect answer. Answer ''yes'' to stop.') # this line was added after reading the solution 