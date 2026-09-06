def sort_age(lst):
    if not lst:
        return []
    sort = []
    for k in lst:
        for i in range(len(sort)):
            if k[1] > sort[i][1]:
                sort.insert(i, k)
                break
        else:
            sort.append(k)
    return sort