value = int (input('enter a value: '))

match value:
    case 5:
        print ('value is 5')

    case 6:
        print ('value is 6')

    case _:
        print ('value is NOT 5 or 6')

