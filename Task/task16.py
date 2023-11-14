# Input: 5 -> 5 1 6 5 9
# Output: 1 9



quantity_wat_mel = int(input("Введиде количество арбузов: "))
wat_mel = [int(input("Введите массу арбузов: ")) for i in range(quantity_wat_mel)]

wat_mel_max = wat_mel[0]
wat_mel_min = wat_mel[0]

for i in range(quantity_wat_mel):
    if wat_mel[i] > wat_mel_max:
            wat_mel_max = wat_mel[i]
    elif wat_mel[i] < wat_mel_min:
            wat_mel_min = wat_mel[i]

print("Масса самого тяжелого арбуза =",wat_mel_max)
print("Масса самого легкого арбуза =",wat_mel_min)