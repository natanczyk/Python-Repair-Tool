def top_k(lst, k):
    max_val = lst[0]
    for i in lst:
        if i > max_val:
            max_val = i
    
    lst2 = []
    while len(lst2) < k:
        max_val = max(lst)
        lst2.append(max_val)
        lst.remove(max_val)
    
    return sorted(lst2, reverse=True)