def top_k(lst, k):
    tmp = []
    # Create a copy of the list to avoid mutating the original input
    lst_copy = list(lst)
    while len(lst_copy) > 0:
        m = max(lst_copy)
        tmp.append(m)
        lst_copy.remove(m)
    return tmp[:k]