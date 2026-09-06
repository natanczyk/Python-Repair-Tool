def top_k(lst, k):
    newlist = []
    while len(newlist) < k:
        max_val = max(lst)
        newlist.append(max_val)
        lst.remove(max_val)
    return newlist