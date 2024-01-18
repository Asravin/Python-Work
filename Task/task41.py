num = int(input("Введите натуральное число: "))
list = list()

for i in range(num):
    sum = 0
    for j in range(1, i // 2 + 1):
        if i % j == 0:
            sum += j
    list.append(tuple([i, sum]))

for i in range(len(list)):
    for j in range(i, len(list)):
        if i != j and list[i][0] == list[j][1] and list[i][1] == list[j][0]:
            print("Дружественные числа, числа", num, ":", *list[i])