def top_k(lst, k):
    i = 0
    while i < len(lst):
        if i + 1 < len(lst) and lst[i] < lst[i + 1]:
            lst[i], lst[i + 1] = lst[i + 1], lst[i]
            i = 0
        else:
            i += 1
    
    return sorted(lst, reverse=True)[:k]