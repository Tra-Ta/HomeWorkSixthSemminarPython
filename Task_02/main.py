# Определить индексы элементов массива (списка), значения 
# которых принадлежат заданному диапазону 
# (т.е. не меньше заданного минимума и не больше заданного максимума)

from random import randint

size = int(input('Введите размер массива -> '))
list_one = []
i = 0
count = 0

while i < size:
    list_one.append(randint(0, 10))
    i += 1

print(list_one)

list_two = []

min_number = int(input('Введите минимальное значение диапазона -> '))
max_number = int(input('Введите максимальное значение диапазона -> '))

for i in range(len(list_one)):
    if min_number <= list_one[i] <= max_number:
        list_two.append(i)

print(f'Индексы элементов принадлежащие заданному диапазону {list_two}')