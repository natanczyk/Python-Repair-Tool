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
    
    # Recursively sort higher and lower parts
    sorted_higher = top_k(higher, len(higher)) if higher else []
    sorted_lower = top_k(lower, len(lower)) if lower else []
    
    sort_list = sorted_higher + plist + sorted_lower
    
    return sort_list[:k]