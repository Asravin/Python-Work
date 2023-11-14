i = int(input("Введите неотрицательное значение факториала: "))
factorial = 1
while i > 0:
    factorial *= i
    i -= 1
print(factorial)