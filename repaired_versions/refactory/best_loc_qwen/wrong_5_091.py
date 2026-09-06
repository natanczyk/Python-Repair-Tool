def top_k(lst, k):
    lst2 = []
    max_val = float('-inf')
    
    for _ in range(k):
        for i in lst:
            if i > max_val:
                max_val = i
        lst2.append(max_val)
        lst.remove(max_val)
        max_val = float('-inf')
    
    return lst2