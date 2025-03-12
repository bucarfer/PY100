'''Without running the following code, determine what will be printed.'''

sale = True
admission_price = 5.25 if not sale else 3.99

print(f"${admission_price}")

# '5.25' is the value for 'not sale', therefore since sale is truthy the admission_price value printe will be '3.99'

# Launch answer:
# In the given code, we're using a conditional expression. The expression checks the value of sale. If sale is False, not sale is True, and admission_price is assigned the value 5.25. If sale is True, not sale is False, and admission_price will be 3.99.