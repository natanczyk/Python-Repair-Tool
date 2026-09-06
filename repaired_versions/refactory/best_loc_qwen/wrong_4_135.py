def sort_age(lst):
    if lst == []:
        return []
    new = []
    max_age = lst[0][1]
    for i in range(1, len(lst)):
        if lst[i][1] > max_age:
            max_age = lst[i][1]
    for item in lst:
        if item[1] == max_age:
            new.append(item)
            lst.remove(item)
    new.extend(sort_age(lst))
    return new