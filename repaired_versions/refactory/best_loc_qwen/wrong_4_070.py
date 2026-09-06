def sort_age(lst):
    if not lst:
        return []
    
    store = []
    while lst:
        oldest = lst[0]
        for i in lst[1:]:
            if i[1] > oldest[1]:
                oldest = i
        store.append(oldest)
        lst.remove(oldest)
    
    return store