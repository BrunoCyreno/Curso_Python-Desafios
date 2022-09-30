import random
print('Welcome to the Divination Game! I will think of a number from 0 to 10. If you can guess what number I chose, you win!')
numberchosen = int(random.randrange(10))
print(numberchosen)
choice = int(input('Choose a number, from 0 to 10: '))
if choice == numberchosen:
    print('You won! Congratulations!')
else:
    print(f'You lost! I chose the number {numberchosen}!')
print('END')

