# What is the output when we run this code?

number = 10
if number >= number:
    print("`if` branch ran!")
elif number > 5:
    print("`elif` branch ran!")
else:
    print("`else` branch ran!")

## Bonus Questions ##
# 1. What would happen if we changed the condition to `number <= number`? 
# Nothing will happen since the number stills equal 

# 2. How do we know which branch will run when multiple conditions evaluate to `True`? 
# the first True condition will run, it goes in order

# 3. Can you explain when `else` branches run? 
# else branch runs when non of the previous conditions are True
