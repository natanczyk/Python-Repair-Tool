def sort_age(lst):
    if len(lst) == 0:
        return []
    elif len(lst) == 1:
        return lst
    else:
        temp = lst[0]
        for i in range(1, len(lst)):
            if lst[i][1] > temp[1]:
                temp = lst[i]
        result = [temp, ]
        lst.remove(temp)
        return [temp] + sort_age([x for x in lst])