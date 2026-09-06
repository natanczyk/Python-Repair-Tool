def sort_age(lst):
    sort = []
    # Create a copy of the list to avoid mutating the original input
    temp_lst = list(lst)
    while temp_lst: 
        # We want the oldest person first, so we look for the maximum age
        largest = temp_lst[0]
        for element in temp_lst:
            # Compare based on the second element of the tuple (age)
            if element[1] > largest[1]:
                largest = element
        temp_lst.remove(largest)
        sort.append(largest)
    return sort