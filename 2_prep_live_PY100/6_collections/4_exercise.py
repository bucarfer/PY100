# You have a dictionary representing inventory items and 
# their quantities. Write a Python function that takes an 
# item and a quantity as input and updates the dictionary 
# by adding the quantity to the existing value (or adds a 
# new item if it doesn’t exist).

'''inventory = {"apples": 10, "bananas": 5, "oranges": 8}

def update_inventory(item, quantity):
    # Your code here'''

## Bonus Questions ##
# 1. Does your code mutate the `inventory` dictionary? Why? 
#    did you make the choice?
# 2. What happens if you pass a negative number as the 
#    `quantity`? Can you account for this with your code?
# 3. What would happen if we accidentally reverse our 
#    arguments when invoking `update_inventory`?

inventory = {"apples": 10, "bananas": 5, "oranges": 8}

def update_inventory(item, quantity):
    inventory[item] = quantity 
    return inventory 

update_inventory('yogurt', -4)
update_inventory('apples', 6)
print(inventory)

# Bonus 1
# yes, because it modifies the original parameter
# yes, I made that decision and I used the same name

# Bonus 2
# it prints the quantity as a negative number, we could convert the quantity to a positive number 

def update_inventory(item, quantity = 'NA'):
    # if quantity < 0:
        # quantity = -quantity
    inventory[item] = quantity 
    return inventory 

update_inventory('yogurt', -4)
update_inventory('apples', 6)
print(inventory)

# Bonus 3
# that Python will save the key and the value with inverted values
update_inventory(7, 'rib-eye')
update_inventory('rib-eye')
print(inventory)

# with the Bonus 2 part where we change all quantities to a positive number, it will raise an error if quantity is not a value 