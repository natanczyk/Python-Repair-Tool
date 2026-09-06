def sort_age(lst):
    if lst == []:
        return []
    new = []
    big = lst[0][1]
    for i in range(1,len(lst)):
        if lst[i][1]>big:
            big = lst[i][1]
    for i in range(len(lst)):
        if lst[i][1] == big:
            new.append(lst[i])
    for i in range(len(new)):
        lst.remove(new[i])
    return new + sort_age(lst)