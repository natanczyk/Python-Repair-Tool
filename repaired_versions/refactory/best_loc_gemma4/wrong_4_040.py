def sort_age(lst):
    
    # Create a copy of the list to avoid modifying the original input list
    temp_lst = list(lst)
    sort_lst = []
    
    while temp_lst:
        smallest = temp_lst[0]
        for element in temp_lst:
            if element[1] < smallest[1]:
                smallest = element
        temp_lst.remove(smallest)
        sort_lst.append(smallest)
    
    # reverse() modifies the list in-place and returns None.
    # We must call it first, then return the list.
    sort_lst.reverse()
    return sort_lst