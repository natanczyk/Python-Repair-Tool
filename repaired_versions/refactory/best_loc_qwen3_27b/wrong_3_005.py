def remove_extras(lst):
    if not lst:
        return []
    length = len(lst)
    result = [lst[0]]
    for i in range(1, length):
        if lst[i] not in result:
            result = result + [lst[i]]
    return result