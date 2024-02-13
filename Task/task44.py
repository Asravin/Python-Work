transformation = lambda sum_list : sum_list
values = [2, 3, 5, 7, 11, 13, 17, 19, 23, 29]
trans_values = set(map(transformation, values))
print(trans_values)