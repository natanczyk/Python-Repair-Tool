def top_k(lst, k):
    new_list = []
    for i in range(k):
        max_val = max(lst)
        new_list.append(max_val)
        lst.remove(max_val)
    return new_list