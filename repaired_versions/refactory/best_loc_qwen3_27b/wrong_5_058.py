def top_k(lst, k):
    # Create a copy of the list to avoid modifying the original
    working_lst = lst[:]
    new_lst = []
    for i in range(k):
        if not working_lst:
            break
        max_val = max(working_lst)
        new_lst.append(max_val)
        # Remove one occurrence of the max value
        working_lst.remove(max_val)
    return new_lst