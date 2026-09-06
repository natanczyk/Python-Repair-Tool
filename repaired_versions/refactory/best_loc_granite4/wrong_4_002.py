def sort_age(lst):
    sorted_list = []
    while lst:
        oldest = lst[0]
        for person in lst:
            if person[1] > oldest[1]:  # Compare ages (index 1)
                oldest = person
        lst.remove(oldest)
        sorted_list.append(oldest)
    return sorted_list