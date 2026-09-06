def sort_age(lst):
    if not lst:
        return []
    list1 = []
    for i in range(len(lst)):
        for j in range(i + 1, len(lst)):
            if lst[i][1] < lst[j][1]:
                lst[i], lst[j] = lst[j], lst[i]
    for i in range(len(lst)):
        list1.append(lst[i])
    return list1