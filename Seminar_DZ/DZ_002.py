'''
2. Создайте программу для игры в "Крестики-нолики".
'''

list = [1,2,3,4,5,6,7,8,9]
game = lambda mass: print(' | ', mass[0], ' | ', mass[1], ' | ', mass[2], ' | \n | ', 
                          mass[3], ' | ', mass[4], ' | ', mass[5], ' | \n | ',
                          mass[6], ' | ', mass[7], ' | ', mass[8], ' | ')
k = 0

def win(mass):
    if (mass[0] == mass[1] == mass[2] == 'X') or (mass[3] == mass[4] == mass[5] == 'X') or (
        mass[6] == mass[7] == mass[8] == 'X') or (mass[0] == mass[3] == mass[6] == 'X') or (
        mass[1] == mass[4] == mass[7] == 'X') or (mass[2] == mass[5] == mass[8] == 'X') or (
        mass[0] == mass[4] == mass[8] == 'X')  or (mass[2] == mass[4] == mass[6] == 'X'):
        return 1        
    elif (mass[0] == mass[1] == mass[2] == 'O') or (mass[3] == mass[4] == mass[5] == 'O') or (
          mass[6] == mass[7] == mass[8] == 'O') or (mass[0] == mass[3] == mass[6] == 'O') or (
          mass[1] == mass[4] == mass[7] == 'O') or (mass[2] == mass[5] == mass[8] == 'O') or (
          mass[0] == mass[4] == mass[8] == 'O')  or (mass[2] == mass[4] == mass[6] == 'O'):
        return 1        
    else: return 0

print("Игра Крестики - нолики")
game(list)
while k <= 9:
    k += 1
    x1 = int(input("Ход игрока №1. В какое поле ставим X: "))
    if list[x1-1] == 'X' or list[x1-1] == 'O':
        x1 = int(input("Поле занято. Введите номер свободного поля: "))
        list[x1-1] = 'X'
    else:
        list[x1-1] = 'X'
    game(list)    
    if win(list):
        print('Игрок №1 победил!') 
        break
    if k == 9: 
        break
    k += 1
    x1 = int(input("Ход игрока №2. В какое поле ставим O: "))
    if list[x1-1] == 'X' or list[x1-1] == 'O':
        x1 = int(input("Поле занято. Введите номер свободного поля: "))
        list[x1-1] = 'O'
    else:
        list[x1-1] = 'O'
    game(list)    
    if win(list): 
        print('Игрок №2 победил!')
        break
if win(list): 
    print("Спасибо за игру!") 
else:
    print("Ничья! Спасибо за игру!")
