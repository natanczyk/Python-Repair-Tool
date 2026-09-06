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
    sort_list = sorted(higher, reverse=True) + plist + sorted(lower, reverse=True)
    
    if k == len(lst):
        return sort_list
    elif k > len(lst):
        return sort_list
    else:
        return sort_list[:k]