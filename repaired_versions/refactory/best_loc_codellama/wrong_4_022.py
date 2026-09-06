def sort_age(lst):
    sort = []
    while lst:
        biggest = lst[0]
        for element in lst:
            if element[1] > biggest[1]:
                biggest = element
        sort.append(biggest)
        lst.remove(biggest)
    return sort