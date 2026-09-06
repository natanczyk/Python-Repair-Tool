def sort_age(lst):
    # Create a copy of the list to avoid mutating the original input
    lst_copy = list(lst)
    sort = []
    while lst_copy:
        oldest = lst_copy[0]
        for person in lst_copy:
            if person[1] > oldest[1]:
                oldest = person
        lst_copy.remove(oldest)
        sort.append(oldest)
    return sort