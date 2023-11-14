days = int(input("Введиде количество дней: "))
count = 0

for i in range(days):
    temp = int(input("Введите показатели температуры: "))
    if temp > 0 | temp < 50:
        count += 1
        
print("Дней с температурой выше 0:", count)
    