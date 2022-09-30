sex = str(input('What is your sex (M or F)? ')).strip() .upper() [0]
while sex not in 'MF':
    print('invalid')
    sex = str(input('What is your sex (M or F)? ')).strip().upper()[0]
'''else:
    print('thank you')'''
print('thank you')