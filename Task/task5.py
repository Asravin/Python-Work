dist = int(input("Введите расстояние пути: "))
speed = int(input("Введите количество км. которое машина проезжает в сутки: "))
time = dist * 24 / speed
day = time // 24
clock = time - day * 24
print(int(day), "дня", int(clock), "часов")