from random import randint
from time import sleep
total = 0
print('the computer will now generate six random numbers: ')
for randomnumbers in range(1, 7):
    sleep(1)
    number = randint(1, 100)+1
    print(number)
    if number % 2 == 0:
        total += number
sleep(2)
print('the sum of all even numbers totals to:', total)