def top_k(lst, k):
    new = []
    for i in range(k):
        max_value = max(lst)
        max_index = lst.index(max_value)
        new.append(lst.pop(max_index))
        
    return new