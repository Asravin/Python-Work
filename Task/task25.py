from random import randint
quan = int(input("Введите количество элементов списка: "))
list = [randint(1, 9) for i in range(quan)]
print("Список элементов:")
print(list)

num = int(input("Введите число поиска: "))
list = set(list)
count = 0
if num > max(list):
    print(max(list))
elif num < min(list):
    print(min(list))
else:
    
    while True:
        if num - count in list and num + count in list and num - count != num + count:
            print(num - count, num + count)
            break
        elif num - count in list:
            print(num - count)
            break
        elif num + count in list:
            print(num + count)
            break
        else:
            count += 1
        