first_num = int(input("Введите первое число: "))
second_num = int(input("Введите второе число: "))

def exponentiation(first_num, second_num):
    if second_num == 0:
        return 1
    return first_num *exponentiation(first_num, second_num - 1)

print(exponentiation(first_num, second_num))