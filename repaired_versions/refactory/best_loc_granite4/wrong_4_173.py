def sort_age(lst):
    sort = []
    while lst:
        max_age = lst[0][1]
        max_index = 0
        for i in range(len(lst)):
            if lst[i][1] > max_age:
                max_age = lst[i][1]
                max_index = i
        sort.append(lst[max_index])
        lst.pop(max_index)
    return sort