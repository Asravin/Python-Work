num_of_coins = int(input("Введите количество монет: "))
from random import randint
coins_zero = 0
coins_one = 0

print("Набор монет:")

for i in range(num_of_coins):
    coin = randint(0, 1)
    print(coin, end = " ")
    if coin == 0:
        coins_zero += 1
    else:
        coins_one += 1

print()

if coins_one >= coins_zero:
    print("Перевеврените монеты 'Орел'", coins_zero, "раз(а)")
else:
    print("Перевеврените монеты 'Решка'",coins_one, "раз(а)")


       