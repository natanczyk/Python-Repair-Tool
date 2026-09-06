def top_k(lst, k):
    # Create a copy of the list to avoid modifying the original input
    temp_lst = list(lst)
    r = []
    for _ in range(0, k):
        if not temp_lst:
            break
        biggest = temp_lst[0]
        for val in temp_lst:
            if biggest < val:
                biggest = val
        r.append(biggest)
        temp_lst.remove(biggest)
    return r