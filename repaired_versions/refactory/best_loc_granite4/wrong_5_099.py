def top_k(lst, k):
    if k > len(lst):
        return False
    if k == 0:
        return []
    if k == 1:
        return [max(lst)]
    
    a = max(lst)
    lst.remove(a)
    return [a] + top_k(lst, k - 1)