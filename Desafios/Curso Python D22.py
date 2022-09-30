name = str(input('type your full name: ')).strip()
# the .strip() command is used to clean spaces before and after a string
print('your name analysis... ')
print(f'your name in uppercase: {name.upper()}')
print(f'your name in lowercase: {name.lower()}')
print(f'your name has this many letters: {len(name)-name.count(" ")}')
# you have to use double quotes for the .count to work
print(f'your first name has this many letters: {name.find(" ")}')
# by finding the position of the first space, you can show how many letters the first name has



