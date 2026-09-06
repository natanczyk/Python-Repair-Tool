def remove_extras(lst):
    if not lst:  # Check if the list is empty
        return []
    result = [lst[0]]
    for i in range(1, len(lst)):
        if lst[i] not in result:
            result = result + [lst[i]]
    return result