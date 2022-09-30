from random import randint
itens=('rock', 'paper', 'scissors')
bot = randint(0, 2)
print('''Choose your play:
[1] Rock
[2] Paper
[3] Scissors''')
player=int(input('what is your play? '))
print('-='*10)
print(f'''bot chose {itens[bot]}
player chose {itens[player]}''')
print('-=' * 10)
if bot == 1 and player == 3:
    print('rock beats scissors. You lost!')
elif bot == 2 and player == 1:
    print('paper beats rock. You lost!')
elif bot == 3 and player == 2:
    print('scissors beats paper. You lost!')
elif bot == player:
    print("it's a draw!")
else:
    print('you won!')