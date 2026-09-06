def sort_age(lst):
    # Create a copy of the list to avoid modifying the original
    old_lst = lst[:]
    new_lst = []
    while old_lst:
        largest = old_lst[0]
        for i in old_lst:
            # Compare by age (second element of tuple) only
            if i[1] > largest[1]:
                largest = i
        old_lst.remove(largest)
        new_lst.append(largest)
    return new_lst