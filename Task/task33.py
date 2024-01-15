def searcher(marks):
    max_num = 0
    min_num = 5
    for i in marks:
        if i < min_num:
            min_num = i
        elif i < max_num:
            max_num = i
            
    return min_num, max_num

def changer(*marks):
    result = searcher(marks)
    min_num, max_num = result[0], result[1]
    marks = list(marks)
    
    for i in range(len(marks)):
        if marks[i] == max_num:
            marks[i] = min_num
    return marks

print(changer(1, 3, 3, 3, 1))