vreal=float(input('how many Reais to be converted: R$ '))
currentdollar=float(input('current quotation of the Dollar: US$ '))
vdollar=vreal/currentdollar
print(f'{vreal} Reais is worth {vdollar:.2f} Dollars.')
