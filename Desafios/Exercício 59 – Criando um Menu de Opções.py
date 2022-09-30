value1 = int(input('first value: '))
value2 = int(input('second value: '))
option = 0
while option != 5:
    print('''
    Options:
    
    [ 1 ] add
    
    [ 2 ] multiply
    
    [ 3 ] greater than
    
    [ 4 ] new numbers
    
    [ 5 ] exit program''')
    option = int(input('>>>>>>>> option: '))
    if option == 1:
        result = value1+value2
        print(f'the sum of {value1} and {value2} is {result}')
    if option == 2:
        result = value1 * value2
        print(f'the multiplication of {value1} and {value2} is {result}')
    if option == 3:
        if value1 > value2:
            print(f'{value1} is greater than {value2}')
        elif value1 < value2:
            print(f'{value2} is greater than {value1}')
        else:
            print('the numbers are equal')
    if option == 4:
        value1 = int(input('new first value: '))
        value2 = int(input('new second value: '))

print ('program ended by the user')

