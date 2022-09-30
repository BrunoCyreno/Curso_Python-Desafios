number = int(input('choose a number: '))
print('''Choose a base for conversion:
[1] Binary conversion
[2] Hexadecimal conversion
[3] Octal conversion''')
choice = int(input(''))
if choice == 1:
    print(f'{number} in binary: {bin(number) [2:]}')
elif choice == 2:
    print(f'{number} in hexadecimal: {hex(number)[2:]}')
elif choice == 3:
    print(f'{number} in octal: {oct(number)[2:]}')
else:
    print('invalid option. Please try again.')