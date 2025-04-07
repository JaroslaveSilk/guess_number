from random import randint as rnd


number = rnd(1, 100)
print('Угадайте число от 1 до 100')

while True:
    players_num = int(input('Введите предполагаемый ответ: '))
    if players_num == number:
        print('Вы угадали число!!!')
        break
    elif players_num > number:
        print('Ваше число больше загаданного =(')
    else:
        print('Ваше число меньше загаданного =(')