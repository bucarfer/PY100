'''Loop over the elements of the fish_list list below, logging each one. Terminate the loop immediately after printing the string 'Nemo'.'''

fish_list = ['Dory', 'Marlin', 'Gill', 'Nemo', 'Bruce']

for fish in fish_list:
    print (fish)
    if fish is 'Nemo': # 'is' or '==' , noth work
        break

''' using a while loop instead:

fish = 0

while fish <= 3:
    print (fish_list[fish])
    fish += 1
'''