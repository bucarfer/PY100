# Predict the output of this snippet and explain why.
num1 = 1
lst1 = [num1, 2, 3]

num1 = 42

print(lst1)  # What is output by this line?
# the output is [1, 2, 3] 
# When we create the lst1 it holds the value "1", lists do not hold variables. Therefore changing num1 doesn't affect lst1

lst1[0] = 42

print(lst1)  # What is output by this line?
# the output is [42, 2, 3]. Here with index reassignment we have mutated the list and pointed the index to a new value.

## Bonus Questions ##
# 1. Does `lst1` contain the variable `num1` as an element?
# 2. Is there anything we can do to `num1` to change the value 
#    at index 0 in our list?
# 3. What could we do instead of line 10 (lst1[0] = 42) that would 
#    have the same outcome on line 12?

# Bonus 1.
# No, the list does not contain the variable as a reference, it contains the value '1' referenced by the variable num1. 

# Bonus 2.
# No, because index 0 in our list is not pointing to num1, it is pointing to the value '1'.

# Bonus 3.
# Reassignment the whole lst1 to a new list in the memory.
lst1 = [42, 2, 3]
print(lst1) #[42, 2, 3]

# LS: a better approach would be to use slicing
lst1 [:1] = [42]
print(lst1) #[42, 2, 3]