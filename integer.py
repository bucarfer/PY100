def range_value (value):
    if value <= 50 and value >= 0:
        print (f' {value} is between 0 and 50')
    elif value > 50 and value <= 100:
        print (f' {value} is between 51 and 100')
    elif value > 100: 
        print (f' {value} is greater than 100')
    else:
        print (f' {value} is less than 0')

range_value (0)
range_value (25)
range_value (50)
range_value (75)
range_value (100)
range_value (101)
range_value (-1)
