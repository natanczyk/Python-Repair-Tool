def remove_extras(lst):
    
    result = lst.copy()
    seen = set()
    i = 0
    
    while i < len(result):
        if result[i] in seen:
            result.pop(i)
        else:
            seen.add(result[i])
            i += 1
            
    return result