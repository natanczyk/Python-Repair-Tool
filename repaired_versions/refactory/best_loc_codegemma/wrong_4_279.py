def sort_age(lst):
    for i in range(len(lst)):
        for j in range(0, len(lst) - i - 1):
            if lst[j][1] < lst[j + 1][1]:
                x = lst[j]
                lst[j] = lst[j + 1]
                lst[j + 1] = x
    return lst