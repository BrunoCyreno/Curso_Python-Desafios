from random import randint
from time import sleep
print('=-=-=-=-=-=-=-=-=-=')
print('  DIVINATION GAME')
print('=-=-=-=-=-=-=-=-=-=')
sleep(1)
print('the goal of the game is to try and divinate a number between 1 and 10 chosen randomly by the computer...')
sleep(1)
pc_choice = randint (1,11)
print(pc_choice)
choice = int(input('Choose a number between 1 and 10: '))
tries = 0
while choice != pc_choice:
    while choice > 10:
        print('you must choose a number between 1 and 10!')
        choice = int(input('Choose a number between 1 and 10: '))
    choice = int(input(' Wrong choice! Try again: '))
    tries += 1

sleep(1)
print('=-=-=-=-=-=-=-=-=-=-=-=-=-=')
print(' YOU WON! CONGRATULATIONS!')
print('=-=-=-=-=-=-=-=-=-=-=-=-=-=')
sleep(1)
print(f'it took {tries} tries')