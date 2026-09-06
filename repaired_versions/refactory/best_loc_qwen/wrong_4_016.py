def sort_age(lst):
    sort = []
    while lst: 
        biggest = lst[0]
        for element in lst:
            if element[1] > biggest[1]:  # Compare ages instead of tuples
                biggest = element
        lst.remove(biggest)
        sort.append(biggest)
    return sort