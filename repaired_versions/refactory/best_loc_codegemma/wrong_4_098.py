def sort_age(lst):
    for i in range(len(lst)):
        for j in range(i+1, len(lst)):
            if lst[i][1] < lst[j][1]:
                temp = lst[i]
                lst[i] = lst[j]
                lst[j] = temp
    return lst