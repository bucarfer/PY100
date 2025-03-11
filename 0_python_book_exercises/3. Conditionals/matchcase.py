value = int (input ('insert value: '))

match value:
    case 1 | 2 | 3 | 4:
        print ('value is < 5')
    case 5 | 6:
        print ('value is 5 or 6')
    case _:
        print ('value is > 6')



