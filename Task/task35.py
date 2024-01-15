num = int(input("Введите число: "))


def reverse(numbers):
    if(numbers == 0):
        return ""
    print(numbers % 10, end= "")
    reverse(numbers // 10)

reverse(num)