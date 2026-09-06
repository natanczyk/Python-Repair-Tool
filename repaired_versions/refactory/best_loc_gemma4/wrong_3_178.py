def remove_extras(lst):
    # Create a new list to store unique elements while preserving order
    result = []
    for item in lst:
        if item not in result:
            result.append(item)
    return result