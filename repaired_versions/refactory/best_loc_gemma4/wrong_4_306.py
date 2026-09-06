def sort_age(lst):
    # Create a copy of the list to avoid modifying the original input list
    temp_lst = list(lst)
    sort = []
    while temp_lst:
        # We want the oldest person at the front, so we find the maximum age
        largest = temp_lst[0]
        for i in temp_lst:
            # Compare based on the second element of the tuple (age)
            if i[1] > largest[1]:
                largest = i
        temp_lst.remove(largest)
        sort.append(largest)
    return sort