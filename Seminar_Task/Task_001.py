'''
1. В файле находится N натуральных чисел, записанных через пробел.
Среди чисел не хватает одного, чтобы выполнялось условие A[i] - 1 = A[i-1].
Найдите это число.
'''

file = open('D:\\OneDrive\\Рабочий стол\\GeekBrains\\005_Знакомство с языком Python\\Seminar_005\\Seminar_Task\\file_task1.txt', 'r')
lst = list(map(int, file.readline().split()))
print(f'Заданный список чисел - {lst}')

for i in range(1, len(lst)):
    if lst[i] - 1 != lst[i - 1]:
        print (f'Не хватает числа - {lst[i]-1}')

file.close()
