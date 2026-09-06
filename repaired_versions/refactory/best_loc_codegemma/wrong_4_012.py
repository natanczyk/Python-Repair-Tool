def sort_age(lst):
    old_lst = lst[:]  # Create a copy of the list
    new_lst = []
    while old_lst:
        largest = old_lst[0]
        for i in old_lst:  # Iterate over the copied list
            if i[1] > largest[1]:  # Compare by age (second element of tuple)
                largest = i
        old_lst.remove(largest)
        new_lst.append(largest)
    return new_lst