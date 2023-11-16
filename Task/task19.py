number = int(input("Введите число возводимое в степень: "))
exponentiation = int(input("Введите число степени: "))
exp_num = 0
print("Число", number, ",", "Степени числа", exponentiation)
while number ** exp_num <= exponentiation:
    print(number ** exp_num, end= " ")
    exp_num += 1