def same(characteristic, objects):
    if len(objects) == 0:
        return True
    characteristic_list = list(map(characteristic, objects))
    
    for i in range(len(characteristic_list) - 1):
        if characteristic_list[i] != characteristic_list[i + 1]:
            return False
        return True

value = [int(input("Введите элементы списка: ")) for i in range(int(input("Введите количество объектов в списке: ")))]
if same(lambda x: x % 2, value):
    print("same")
else:
    print("different")


