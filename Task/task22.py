dict = [
    {"V": "S001"}, 
    {"V": "S002"}, 
    {"VI": "S001"}, 
    {"VI": "S005"}, 
    {"VII": "S005"}, 
    {"V": "S009"}, 
    {"VIII": "S007"}
    ]

dictionary = set(keys for word in dict for keys in word.values())
print("Уникальные значения словаря: ", dictionary)

