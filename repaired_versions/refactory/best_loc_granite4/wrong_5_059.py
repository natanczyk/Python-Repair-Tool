def top_k(lst, k):
    new_lst = []
    for i in range(k):
        max_val = max(lst)
        lst.remove(max_val)
        new_lst.append(max_val)
    return new_lst