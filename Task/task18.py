one_num = int(input("Введите первое число: "))
two_num = int(input("Введите второе число: "))
print('*' * 20)
for i in range(one_num):
    for j in range(two_num):
        if one_num == i + j and two_num == i * j:
            print("Загаданное число:", i)
