def finder(number):
    for i in range(2, number):
        if number % i == 0:
            return "NO"
    return "YES"

number = int(input("Введите число: "))
print(finder(number))