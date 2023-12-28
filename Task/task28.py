sentence = input("Введите текст: ")
text = set()
word = ''
for i in sentence:
    if i not in{' ', ',', '.', '!', '?', ':', ';'}:
        word += i
    else:
        if word != '':
            text.add(word)
        word = ""
print("Количество слов в тексте:", len(text))