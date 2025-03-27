# What happens when we run this code? How are lines 3 and 4 different?

score = 100
score += 50
score = score + 50

print(score)
# 200

## Bonus Questions ##
# 1. How many `score` variables exist in this code snippet?
# 1 variable since we are using reassignment that doesn't create a new variable, it changes the value of the existing variable 

# 2. If they have the same behavior, which line is preferable, 3 or 4? 3 is preferable because there is less room to error

# 3. What other data types can we use `+=` with? What is this called?
# they are called augmented assignment and can be also used with strings, or lists. the most common use is strings or numeric values
