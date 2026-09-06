def sort_age(lst):
    sort = []
    while lst:
        max_index = 0
        for i in range(1, len(lst)):
            if lst[i][1] > lst[max_index][1]:
                max_index = i
        sort.append(lst.pop(max_index))
    return sort