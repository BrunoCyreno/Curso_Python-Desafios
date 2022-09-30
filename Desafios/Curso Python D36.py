house = float(input('price of the house: '))
salary = float(input('your monthly salary: '))
years = int(input('how many years to pay: '))
monthsinyear = float(years*12)
monthlyvalue = float(house/monthsinyear)
percentofsalary = salary*30/100
if monthlyvalue <= percentofsalary:
    print('your loan was approved')
else:
    print('your loan was denied')




