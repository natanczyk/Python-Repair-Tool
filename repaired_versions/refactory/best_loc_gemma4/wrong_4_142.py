def sort_age(lst):
    # Create a copy of the list to avoid modifying the original input list
    lst_copy = list(lst)
    sort = []
    while lst_copy:
        oldest = lst_copy[0]
        for i in lst_copy:
            # Change < to > to find the maximum age instead of the minimum age
            if i[1] > oldest[1]:
                oldest = i
        lst_copy.remove(oldest)
        sort.append(oldest)
    return sort