def remove_extras(lst):
    if not lst:
        return []
    
    a = []
    seen = set()
    for item in lst:
        if item not in seen:
            a.append(item)
            seen.add(item)
    
    return a