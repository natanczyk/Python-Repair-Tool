def sort_age(lst):
    # Create a copy of the list to avoid mutating the original input
    lst_copy = list(lst)
    sort = []
    while lst_copy:
        biggest = lst_copy[0]
        for k in lst_copy:
            if k[1] > biggest[1]:
                biggest = k
        lst_copy.remove(biggest)
        sort.append(biggest)
    return sort