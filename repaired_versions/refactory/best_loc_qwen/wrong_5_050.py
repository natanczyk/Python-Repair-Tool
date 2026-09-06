def top_k(lst, k):
    newlist = []
    while len(newlist) < k:
        max_val = max(lst)
        max_idx = lst.index(max_val)
        newlist.append(max_val)
        del lst[max_idx]
    return sorted(newlist, reverse=True)