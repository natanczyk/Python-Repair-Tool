def top_k(lst, k):
    new_lst = []
    for i in range(k):
        if not lst:  # If the list is empty, break early
            break
        max_val = max(lst)
        new_lst.append(max_val)
        lst.remove(max_val)  # Remove the max value from the list
    return new_lst