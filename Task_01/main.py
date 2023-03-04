# Задача 30: Заполните массив элементами арифметической прогрессии. 
# Её первый элемент, разность и количество элементов нужно ввести с клавиатуры. 
# Формула для получения n-го члена прогрессии: an = a1 + (n-1) * d.
# Каждое число вводится с новой строки.


def Arifmetic(list, size, first, difference):
    i = 1
    while i < size+1:
        list.append(first + (i-1)*difference)
        i += 1
    return list


list_1 = []
size = int(input('Введите размер массива: '))
first = int(input('Введите первый элемент: '))
difference = int(input('Введите разность элементов: '))

print(Arifmetic(list_1, size, first, difference))