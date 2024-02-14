def counting(text):
    text = text.split()
    list = []
    for word in text:
        count = 0
        for i in word:
            if i in "йуеёыаоэию":
                count += 1
        list.append(count)
    return len(list) == list.count(list[0])

text = input("Введите текст: ")
if counting(text):
    print("Парам пам-пам")
else:
    print("Пам парам")
