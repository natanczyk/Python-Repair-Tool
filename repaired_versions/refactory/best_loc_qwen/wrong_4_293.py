def sort_age(lst):
    sort = []
    while lst:
        biggest = 0
        for i in lst:
            if i[1] > biggest:
                biggest = i[1]
        for i in lst:
            if i[1] == biggest:
                sort.append(i)
                lst.remove(i)
                break
    return sort