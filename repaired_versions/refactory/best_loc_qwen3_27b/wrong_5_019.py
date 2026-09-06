def top_k(lst, k):
    arranged = []
    # Create a copy to avoid modifying the original list
    working_lst = lst[:]
    while k > 0:
        max_val = max(working_lst)
        arranged.append(max_val)
        working_lst.remove(max_val)
        k -= 1
    return arranged