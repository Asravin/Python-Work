first_list = [int(input("Введите количество элементов первого списка: ")) for i in range(int(input("Введите элементы первого списка: ")))]
second_list = [int(input("Введите количество элементов второго списка: ")) for i in range(int(input("Введите элементы второго списка: ")))]
print("Первый список:", first_list)
print("Второй список:", second_list)
print("Во втором списке нет следующих элементов из первого: ")

select_list = []
for i in first_list:
    if i not in second_list:
        print(i)
