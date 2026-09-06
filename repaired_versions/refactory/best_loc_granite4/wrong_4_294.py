def sort_age(lst):
    sort = []
    while lst:
        biggest = lst[0][1]
        max_item = lst[0]
        for i in lst:
            if i[1] > biggest:
                biggest = i[1]
                max_item = i
        lst.remove(max_item)
        sort.append(max_item)
    return sort