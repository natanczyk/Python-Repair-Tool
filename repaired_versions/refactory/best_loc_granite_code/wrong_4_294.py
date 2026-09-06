def sort_age(lst):
    sort = []
    while lst:
        biggest = lst[0][1]
        for i in lst:
            if i[1] >= biggest:
                biggest = i[1]
                max_person = i
        lst.remove(max_person)
        sort.append(max_person)
    return sort