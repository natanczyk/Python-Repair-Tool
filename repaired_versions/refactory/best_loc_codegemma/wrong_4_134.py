def sort_age(lst):
    if lst == []:
        return []
    new = []
    for i in range(len(lst)):
        max_age = lst[0][1]
        max_index = 0
        for j in range(1, len(lst)):
            if lst[j][1] > max_age:
                max_age = lst[j][1]
                max_index = j
        new.append(lst[max_index])
        lst.pop(max_index)
    return new