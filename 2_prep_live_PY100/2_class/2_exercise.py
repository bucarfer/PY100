# What is the output when we run this code?

a = 5
b = 3.2
result = a + b
print(result)

# the output is 8.2

## Bonus Questions ##
# 1. What data type will `result` be, and why? 
# the output will be a float, because one of the summary values is a float, and the addition of both will result in a float 
 
# 2. What would happen if you tried to subtract `b` from `a` instead? 
# you will get a negative float with the difference between them, we can round the rule and say if we do any arithmetic operation with a float it will return a float 

result2 = b - a
print(result2) #-1.79999

# 3. How can you convert `result` to an integer? 
# to convert the result to an integer we can use the constructor 'int' and force an explicit coercion to transform the float back to an integer. A better method to get the rounded number is to use the function "round"

print(int(1.8)) #1
print(round(1.8)) #2