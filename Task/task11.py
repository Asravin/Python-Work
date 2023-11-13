tiket = int(input("Введите номер билета: "))

num1 = tiket % 10
tiket = tiket // 10
num2 = tiket % 10
tiket = tiket // 10
num3 = tiket % 10
tiket = tiket // 10
num4 = tiket % 10
tiket = tiket // 10
num5 = tiket % 10
tiket = tiket // 10


if num1 + num2 + num3 == num4 + num5 + tiket:
    print("Билет счастливый!")
else:
    print("Билет не счастливый")