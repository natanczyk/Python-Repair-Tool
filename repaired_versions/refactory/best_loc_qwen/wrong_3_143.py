def remove_extras(lst):
    for i in range(len(lst)):
        for j in range(i + 1, len(lst)):
            if lst[j] == lst[i]:
                lst.pop(j)
                return remove_extras(lst)
    return lst