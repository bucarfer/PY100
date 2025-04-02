# What happens when we run this code? Try to explain the output.

a = [1, 2, 3]
b = a # we assigned b to the value referenced by a
b.append(4)

print(a) #[1, 2, 3, 4] # I was wrong, my first answer was [1, 2, 3]
print(b) #[1, 2, 3, 4]

# when we append a new object to list b, it will change both lists.
### LS: there is only one object and both variables are assigned to the same list in the memory.

## Bonus Questions ##
# 1. If we reassign `b` to a new list before invoking `append`, what will happen to `a`? Demonstrate with code.
# 2. What would change if we used `+=` instead of `append`?
# 3. If we change an element of the list `b`, how will that affect `a`? Explain with code examples.

# Bonus 1.
# It doesn't affect list a, only list b.
# Each variable was assigned to a different list in the memory as starting point, then the changes will affect only list 'b'.

a = [1, 2, 3]
b = a
b = [1, 2, 3]
b.append(4)

print(a) #[1, 2, 3]
print(b) #[1, 2, 3, 4]

# Bonus 2.
# With augmented assignment, this function mutates the original object when the object is mutable. If the object is immutable it creates a new object. In this case, a list is mutable, so it will mutate list a and b and both will be affected by the change. 
# Same result as main problem. 

a = [1, 2, 3]
b = a
b += [4] # we use augmented assignment on b

print(a) #[1, 2, 3, 4]
print(b) #[1, 2, 3, 4]

# Bonus 3. 
# Index assignment mutates the list by reassigning the index to a new value, therefore list a and b are affected by the change. 
# Same result as main problem. 

a = [1, 2, 3]
b = a
b [1] = 0

print(a) #[1, 0, 3]
print(b) #[1, 0, 3]

# Only in bonus 1 question when we reassign list b to a different list in the memory before mutating the list b, list a is not affected by the changes done in list b and the lists are different.

