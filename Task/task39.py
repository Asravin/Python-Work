list = [int(input("Введите элементы списка: ")) for i in range(int(input("Введите количество элементов списка: ")))]
print(list)
print("Количество соседних элементов меньше данного: ")
count = 0
for i in range(1, len(list) - 1):
    if list[i] > list[i - 1] and list[i] > list[i + 1]:
        count += 1
print(count)