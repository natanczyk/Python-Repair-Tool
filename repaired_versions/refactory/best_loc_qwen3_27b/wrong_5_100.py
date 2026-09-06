def top_k(lst, k):
    l = []
    if k > len(lst):
        return False
    elif k == 0:
        return []
    else:
        # Create a copy to avoid modifying the original list
        lst_copy = lst[:]
        while len(l) < k:
            a = max(lst_copy)
            lst_copy.remove(a)
            l.append(a)
        
        return l