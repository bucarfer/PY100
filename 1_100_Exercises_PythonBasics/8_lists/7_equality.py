'''Predict the output of the code shown below. When you run the code, do you see what you expected? Why or why not?

list1 = [2, 6, 4]
list2 = [2, 6, 4]

print(list1 == list2)'''

list1 = [2, 6, 4]
list2 = [2, 6, 4]

print(list1 == list2)

# the output is True because we are comparing two lists that contain the same values in the same order 

# however sin list1 and list2 are two different objects in memory, the "is" operator will return False: print(list1 is list2) # False 

# the "is" operator checks if whether the two objects are the same object in memory 

# value equality == 
# object equality "is"