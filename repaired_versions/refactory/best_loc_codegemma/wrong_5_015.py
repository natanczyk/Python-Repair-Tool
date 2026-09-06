def top_k(lst, k):
    
    if lst == []:
        return lst
    
    lower = []
    higher = []
    plist = []
    
    pivot = lst[0]
    for e in lst:
        if e < pivot:
            lower.append(e)
        if e == pivot:
            plist.append(e)
        if e > pivot:
            higher.append(e)
    
    lower = top_k(lower, k)
    higher = top_k(higher, k)
    
    sort_list = higher + plist + lower
    
    return sort_list[:k]