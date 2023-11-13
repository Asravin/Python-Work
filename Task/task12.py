length = int(input("Введите длину шоколадки: "))
width = int(input("Введите ширину шоколадки: "))
piece = int(input("Введите количество долек: "))

if piece < length * width and ((piece % length == 0) or (piece % width == 0)):
    print("YES")
else:
    print("NO")