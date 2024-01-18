first_elem = int(input("Введите первый элемент арифметической прогресии: "))
difference = int(input("Введите разность арифметической прогресии: "))
amount = int(input("Введите количество элементов арифметической прогресии: "))
print("Список элементов арифметической прогресии: ")
for i in range(amount):
    print(first_elem + i * difference)
    



