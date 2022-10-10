'''
1. Создайте программу для игры с конфетами человек против человека.    
    Условие задачи: На столе лежит 2021 конфета. Играют два игрока делая ход друг после друга.
    Первый ход определяется жеребьёвкой. За один ход можно забрать не более чем 28 конфет.
    Все конфеты оппонента достаются сделавшему последний ход.
    Сколько конфет нужно взять первому игроку, чтобы забрать все конфеты у своего конкурента?    
    a) Добавьте игру против бота    
    b) Подумайте как наделить бота "интеллектом"    
'''

'''
import random

greeting = ('Здравствуйте! Вас приветствует игра "2021 конфета!" '
            'Основные правила игры: '
            'Договариваемся сколько будет конфет на кону, '
            'за один ход мы можем взять не более определённого количества, '
            'о котором мы договоримся тоже. Победитель забирает ВСЁ) '
            'Погнали...!')

messages = ['Ваша очередь брать конфеты', 'возьмите конфеты', 
            'сколько конфет возьмёте?', 'берите, пожалуйста', 'Ваш ход']

def play_game(n, m, players, messages):
    count = 0
    if n%10 == 1 and 9 > n > 10: letter = 'а'
    elif 1 < n%10 < 5 and 9 > n > 10: letter = 'я'
    else: letter = ''
    while n > 0:
        print(f'{players[count%2]}, {random.choice(messages)}')
        move = int(input())
        if move > n or move > m:
            print(f'Вы взяли много, можно взять не более {m} конфет{letter}, у нас всего {n} конфет{letter}!')
            attempt = 3
            while attempt > 0:
                if n >= move <= m:
                    break
                print(f'Попробуйте ещё раз, у Вас {attempt} попытки')
                move = int(input())
                attempt -=1
            else: 
                return print(f'Очень жаль, Вы истратили 3 попытки( Game over!')
        n = n - move
        if n > 0: print(f'Осталось {n} конфет{letter}')
        else: print('Конфеты закончились.')
        count +=1
    return players[not count%2]

print(greeting)

player1 = input('Давайте знакомится:)\nИгрок №1, как Вас зовут?\n')
player2 = input('Игрок №2, и Вы представьтесь, пожалуйста\n')
players = [player1, player2]

n = int(input('Сколько конфет на кону? '))
m = int(input('Сколько максимально будем брать конфет за один ход? '))

winer = play_game(n, m, players, messages)
if not winer:
    print('У нас нет победителя.')
else: print(f'Поздравляю! Победил {winer}! Ему достаются все конфеты!')
'''

# Вариант - человек vs bot

from random import randint, choice

greeting = ('Здравствуйте! Вас приветствует игра "2021 конфета!" '
            'Основные правила игры: '
            'Нам будет дано некоторое количество конфет, '
            'за один ход мы можем взять не более определённого количества, '
            'о котором мы с вами договоримся. Победитель забирает ВСЁ) '
            'Итак, начнём!')

messages = ['Ваша очередь брать конфеты', 'возьмите конфеты',
            'сколько конфет возьмёте?', 'берите, пожалуйста', 'Ваш ход']

def introduce_players():
    player1 = input('Давайте знакомится:)\nИгрок, как Вас зовут?\n')
    player2 = 'Конфетный обжора'
    print(f'Очень приятно, меня зовут {player2}')
    return [player1, player2]

def get_rules(players):
    n = int(input('Сколько конфет на кону? '))
    m = int(input('Сколько максимально будем брать конфет за один ход? '))
    first = int(input(
        f'{players[0]}, если хотите ходить первым, нажмите 1, если нет, любую другую клавишу\n'))
    if first != 1:
        first = 0
    return [n, m, int(first)]

def play_game(rules, players, messages):
    count = rules[2]
    if rules[0] % 10 == 1 and 9 > rules[0] > 10:
        letter = 'а'
    elif 1 < rules[0] % 10 < 5 and 9 > rules[0] > 10:
        letter = 'ы'
    else:
        letter = ''
    while rules[0] > 0:
        if not count % 2:
            move = randint(1, rules[1])
            print(f'Я забираю {move}')
        else:
            print(f'{players[0]}, {choice(messages)}')
            move = int(input())
            if move > rules[0] or move > rules[1]:
                print(f'Вы взяли много, можно взять не более {m} конфет{letter}, у нас всего {n} конфет{letter}!')
                attempt = 3
                while attempt > 0:
                    if rules[0] >= move <= rules[1]:
                        break
                    print(f'Попробуйте ещё раз, у Вас {attempt} попытки')
                    move = int(input())
                    attempt -= 1
                else:
                    return print(f'Очень жаль, Вы истратили 3 попытки( Game over!')
        rules[0] = rules[0] - move
        if rules[0] > 0:
            print(f'Осталось {rules[0]} конфет{letter}')
        else:
            print('Все конфеты разобраны.')
        count += 1
    return players[count % 2]

print(greeting)

players = introduce_players()
rules = get_rules(players)

winer = play_game(rules, players, messages)
if not winer:
    print('У нас нет победителя.')
else:
    print(
        f'Поздравляю! В этот раз победил {winer}! Ему достаются все конфеты!')
