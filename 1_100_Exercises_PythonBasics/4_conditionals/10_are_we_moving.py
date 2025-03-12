'''Determine what the following code snippet prints. First solve it in your head or on paper, then run it in your Python environment to check the result.

Bonus question: Do we need the parentheses in the boolean expression or could we have written the following?:

is_moving = braking_force < acceleration and speed > 0 or acceleration > 0
'''

speed = 0
acceleration = 24
braking_force = 19
is_moving = braking_force < acceleration and (speed > 0 or acceleration > 0)
print(is_moving)

# in this case the result doesnt change, but without the parenthesis we change the order of the logical operations, plus it is always better to keep the parenthesis to help reading the code
# not, and, or (order from highest to lowest), as shown below:
# is_moving = (braking_force < acceleration and speed > 0) or acceleration > 0