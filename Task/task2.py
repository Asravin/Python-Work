first_num = int(input("Введите первое число: "))
second_num = int(input("Введите второе число: "))

if first_num % 2 == 0:
    print("Первое число четное")
else:
    print("Первое число не четное")

if second_num % 2 == 0:
    print("Второе число четное")
else:
    print("Второе число не четное")
    
if first_num % 2 == second_num % 2 :
    print("Оба введенных числа имеют одинаковую четность ")
else:
    print("Введенные числа имеют разную четность ")
