def remove_extras(lst):
    if not lst:
        return []
    
    result = [lst[0]]
    for item in lst[1:]:
        if item not in result:
            result.append(item)
    return result