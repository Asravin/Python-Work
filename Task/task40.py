list = [int(input("Введите элементы списка: ")) for i in range(int(input("Введите количество элементов списка: ")))]
set = set()
print("Список чисел:", list)
amount = 0
for i in list:
    if i not in set:
        amount += list.count(i) // 2
        set.add(i)
print("Пар элементов в списке равных друг другу:", amount)