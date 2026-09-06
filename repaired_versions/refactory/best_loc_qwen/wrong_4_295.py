def sort_age(lst):
    sort = []
    while lst:
        biggest = lst[0][1]
        index = 0
        for i in range(1, len(lst)):
            if lst[i][1] > biggest:
                biggest = lst[i][1]
                index = i
        sort.append(lst.pop(index))
    return sort