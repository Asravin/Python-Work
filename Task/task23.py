from random import randint
list = [randint(1, 10) for i in range(randint(8, 20))]
print(list)

count = 0
for i in range(0, len(list) - 1):
    if list[i + 1] > list[i]:
        count += 1
print("Количество элементов массива больших преведущего = ", count)