numbers = range(3, 501, 3)
total=0
count=0
for mult in numbers:
    count += 1
    total += mult
print(f'there are {count} multiples of 3 in a range from 1 to 500. The sum of these numbers totals {total} ')