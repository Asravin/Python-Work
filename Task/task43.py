list = [int(input("Введите элементы списка: ")) for i in range(int(input("Введите количество элементов списка: ")))]
print("Изначальный список:", list)
min = int(input("Введите минимальное значение диапазона:"))
max = int(input("Введите максимальное значение диапазона:"))
print("Индексы элементов в заданном диапазоне: ")
for i in range(len(list)):
    if min <= list[i] <= max:
        print(i)
        
        
        
