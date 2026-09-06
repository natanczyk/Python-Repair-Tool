def remove_extras(lst):
    if not lst:
        return []
    a = [lst[0]]
    for j in range(1, len(lst)):
        if lst[j] not in a:
            a.append(lst[j])
    
    return a