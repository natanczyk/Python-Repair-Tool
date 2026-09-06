def top_k(lst, k):
    l = []
    if k > len(lst):
        return False
    elif k == 0:
        return []
    elif k == 1:
        return [max(lst)]
    else:
        a = max(lst)
        lst.remove(a)
        l.append(a)
        rest = top_k(lst, k-1)
        l.extend(rest)
        return l
        
    # Fill in your code here
    pass