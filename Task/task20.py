from random import randint
count = int(input("Введите количество элементов в списке: "))

list = [randint(1, 10) for i in range(count)]
print("Список чисел: ")
list.sort()
print(list)

set = set(list)
print("Количество уникальных значений в списке:")
print(len(set))
