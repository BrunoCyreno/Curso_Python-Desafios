import random
num1=input('name of first sacrifice')
num2=input('name of second sacrifice')
num3=input('name of third sacrifice')
num4=input('name of fourth sacrifice')
candidates=(num1, num2, num3, num4)
selected=random.choice(candidates)
print(f'the sacrifice is {selected}')

