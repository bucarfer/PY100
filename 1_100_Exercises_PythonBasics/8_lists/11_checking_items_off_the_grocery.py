'''We have a grocery list. As we check off items on that list, from the top of the list to the bottom, we want to remove them from the list.

Write code that removes the items from grocery_list, one by one, until it is empty. If you print the elements you remove, the expected behavior would look as follows.

Copy Code
grocery_list = ['paprika', 'tofu', 'garlic', 'quinoa',
                'carrots', 'broccoli', 'hummus']

print(grocery_list)

Expected outputCopy Code
paprika
tofu
garlic
quinoa
carrots
broccoli
hummus
[]'''

#I needed the help of launch school solution, I was trying to use a for loop, and it was skipping some values as explained in the video

grocery_list = ['paprika', 'tofu', 'garlic', 'quinoa',
                'carrots', 'broccoli', 'hummus']

while grocery_list:
    checked_item = grocery_list.pop(0)
    print (checked_item)

print (grocery_list)
