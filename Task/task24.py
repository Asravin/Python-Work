from random import randint
quan = int(input("Введите количество элементов в списке: "))
list = [randint(1, 9) for i in range(quan)]
print("Список:")
print(list)

num = int(input("Введите число поиска: "))
count = 0
for i in range(quan):
    if list[i] == num:
        count += 1
print("Число", num, "встречается в списке", count, "раз(а)")