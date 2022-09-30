from random import randrange
speed = randrange(50, 200)
print(f'your speed is {speed}Km/h')
if speed > 80:
    fine = float(speed-80)
    print(f'you have to pay R${fine*7} for speeding')
else:
    print('You are good to go. Drive safely!')
print('end')
