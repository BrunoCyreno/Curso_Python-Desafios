from time import sleep
number = int(input('write any number:'))
for table in range (1,11):
    print(f'{number}x{table} = {number*table}', end= ' ')
    sleep(1)
print ('END', )