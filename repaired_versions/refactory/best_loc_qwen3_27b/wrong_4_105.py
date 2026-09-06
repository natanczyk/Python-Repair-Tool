def sort_age(lst):
    sort1 = []
    while lst:
        largest = lst[0][1]
        largest_person = lst[0]
        for i in lst:
            if i[1] > largest:
                largest = i[1]
                largest_person = i
        lst.remove(largest_person)
        sort1.append(largest_person)
    return sort1