def sort_age(lst):
    sort = []
    while lst:
        biggest = lst[0][1]
        biggest_index = 0
        for i in range(len(lst)):
            if lst[i][1] >= biggest:
                biggest = lst[i][1]
                biggest_index = i
        sort.append(lst.pop(biggest_index))
    return sort