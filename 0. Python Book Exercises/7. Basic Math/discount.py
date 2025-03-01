value = input('Enter price of item: ')
discount = input ('Enter discount %: ')
total = float(value) * (100 - float(discount)) / 100

print(f'The final price is: {total}')
