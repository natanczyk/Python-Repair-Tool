def sort_age(lst):
    # Create a copy of the list to avoid mutating the original input
    lst_copy = list(lst)
    result = []
    while lst_copy:
        oldest = lst_copy[0]
        for people in lst_copy:
            if people[1] > oldest[1]:
                oldest = people
        lst_copy.remove(oldest)
        result.append(oldest)
    return result