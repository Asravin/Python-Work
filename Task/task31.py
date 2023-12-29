quan = int(input("Введите количество кустов: "))
garden = list()
for i in range(quan):
    bush = int(input("Введите номер куста: "))
    garden.append(bush)

count = list()
for i in range(len(garden) - 1):
    count.append(garden[i - 1] + garden[i] + garden[i + 1])

count.append(garden[-2] + garden[-1] + garden[0])

quan_bush = max(count)
print("Максимальное количество ягод:", quan_bush)
