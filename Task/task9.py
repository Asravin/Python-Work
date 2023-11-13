number = int(input("Введите трехзначное число: "))
num1 = number % 10
number = number // 10
num2 = number % 10
number = number // 10
print("Сумма трехзначного числа =", number + num1 + num2)