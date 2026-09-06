def sort_age(lst):
    sort = []
    while lst:
        biggest = lst[0][1]
        biggest_item = lst[0]
        for i in lst:
            if i[1] > biggest:
                biggest = i[1]
                biggest_item = i
        lst.remove(biggest_item)
        sort.append(biggest_item)
    return sort