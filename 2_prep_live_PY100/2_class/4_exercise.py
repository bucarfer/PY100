# What is the output when we run this code?

x = 10
y = 3
print(x / y) # 3.3333
print(x // y) # 3
print(x % y) # 1



## Bonus Questions ##
# 1. What's the difference between '/' and '//' operators in Python?
# first symbol is the normal division symbol and the second one for division, returns only the highest full divisor number 

# 2. What does the '%' operator do? Can you think of a practical use for it?
# the modular symbol returns the difference between the dividend that can be divided by a full divisor and the original dividend number, "the leftover of a whole division without decimals"

# 3. What data type will each operation return? Why might this be important?
# it will return a float or integer depending on the division
# it will return a float or integer, depending on the original X value type, but the real value will be always a float
#it will return a float 
# the type is important in case we want to continue doing operations and we create an error for incompatibility between types 
