from random import randint
first_list = [randint(1, 99) for i in range(int(input("Введите количество элементов списка: ")))]
print("Первый набор чисел:", first_list)

second_list = [randint(1, 99) for i in range(int(input("Введите количество элементов списка: ")))]
print("Второй набор чисел:", second_list)

first_set = set(first_list)
second_set = set(second_list)

print(first_set)
print(second_set)

set = sorted(first_set.intersection(second_set))
print("В обоих списках встречаются числа:", set)