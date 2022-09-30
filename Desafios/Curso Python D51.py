from time import sleep
print('=========================')
print(' ARITHMETIC PROGRESSION')
print('=========================')
sleep(1)
termone = int(input('first term: '))
sleep(0.5)
commondiference = int(input('common difference: '))
ending = termone+(11-1)*commondiference
sleep(1)
print('progression: ')
for arithmetic in range(termone, ending, commondiference):
    print(arithmetic, end=', ')
    sleep(0.5)
sleep(1)
print(' ')
print('=====')
print(' END')
print('=====')


