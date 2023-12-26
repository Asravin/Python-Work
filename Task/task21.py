from random import randint

quan = int(input("Введите количество элементов списка: "))
num = int(input("Введите число сдвига элементов списка: "))
list = [randint(1, 10) for i in range(quan)]
print("Изначальный список: ")
print(list)

for i in range(num):
    new_list = list[0]
    for i in range(len(list) - 1):
        list[i] = list[i + 1]
    list[-1] = new_list
print("Список с сдвигом на", num, "элементов:")
print(list)