str = input("Введите строку или слово: ")
dict = {}
for letter in str:
    if letter not in dict:
        dict[letter] = 1
    else:
        dict[letter] += 1
print("Количество использованных букв:", dict)