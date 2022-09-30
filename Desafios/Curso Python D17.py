from math import hypot, trunc
opposite=int(input('what is the opposite of the hypotenuse?'))
adjacent=int(input('what is the adjacent of the hypothenuse?'))
hypotenuse=hypot(opposite, adjacent)
print(f'the hypotenuse of this triangle is {hypotenuse:.2f}')
