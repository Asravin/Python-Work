first_num = int(input("Введите первое число: "))
second_num = int(input("Введите второе число: "))


def fun_sum(first_num, second_num):
    if second_num == 0:
        return first_num
    return 1 + fun_sum(first_num, second_num - 1)

print(fun_sum(first_num, second_num))