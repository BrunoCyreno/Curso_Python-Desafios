travel=float(input('distance will you travel in Kilometres: '))
if travel <= 200:
    print(f'you will pay R${(travel*0.50)} for your trip')
else:
    print(f'you will pay R${(travel*0.45)} for your trip')


