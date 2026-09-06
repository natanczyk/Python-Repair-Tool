def top_k(lst, k):

    newlst = []
    for _ in range(k):
        max_val = max(lst)
        newlst.append(max_val)
        lst.remove(max_val)
    return newlst