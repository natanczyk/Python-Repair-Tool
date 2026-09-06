def top_k(lst, k):
    # Create a copy to avoid modifying the original list
    working_lst = lst[:]
    new_lst = []
    for _ in range(k):
        if not working_lst:
            break
        max_val = max(working_lst)
        new_lst.append(max_val)
        working_lst.remove(max_val)
    return new_lst