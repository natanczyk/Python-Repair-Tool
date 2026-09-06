def sort_age(lst):
    sort = []
    while lst: 
        biggest = lst[0]  # Start with the first element
        for element in lst:
            if element[1] > biggest[1]:  # Compare based on age (second element of tuple)
                biggest = element
        lst.remove(biggest)
        sort.append(biggest)
    return sort