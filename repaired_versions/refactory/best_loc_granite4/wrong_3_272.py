def remove_extras(lst):
    if not lst:
        return []
    result = [lst[0]]
    for e in lst[1:]:
        if e not in result:
            result.append(e)
    return result