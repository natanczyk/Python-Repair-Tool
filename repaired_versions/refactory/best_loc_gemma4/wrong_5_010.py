def top_k(lst, k):
    # Create a copy of the list to avoid modifying the original input
    temp_lst = list(lst)
    # We need to remove the smallest elements until only k elements remain
    n_to_remove = len(temp_lst) - k
    counter = 0
    while counter < n_to_remove:
        temp_lst.remove(min(temp_lst))
        counter = counter + 1
    
    # Now extract the remaining k elements in descending order
    sort_list = []
    while temp_lst != []:
        max_val = max(temp_lst)
        sort_list.append(max_val)
        temp_lst.remove(max_val)
    return sort_list