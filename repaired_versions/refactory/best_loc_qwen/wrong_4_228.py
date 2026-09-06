def sort_age(lst):
    if not lst:
        return lst
    
    n = len(lst)
    for i in range(n):
        oldest = lst[i][1]
        idx = i
        for j in range(i+1, n):
            if lst[j][1] > oldest:
                oldest = lst[j][1]
                idx = j
        
        if idx != i:
            lst[i], lst[idx] = lst[idx], lst[i]
    
    return lst