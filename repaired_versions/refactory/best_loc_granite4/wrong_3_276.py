def remove_extras(lst):
    if not lst:  # Check if the list is empty
        return []
    result = [lst[0],]
    for e in lst:
        if e not in result:
            result.append(e)
        else:
            continue
    return result