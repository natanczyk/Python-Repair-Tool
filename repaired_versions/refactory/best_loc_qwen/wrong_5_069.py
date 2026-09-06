def top_k(lst, k):
    new = []
    while len(new) < k:
        max_val = lst[0]
        for num in lst:
            if num > max_val:
                max_val = num
        new.append(max_val)
        lst.remove(max_val)
        
    return sorted(new, reverse=True)