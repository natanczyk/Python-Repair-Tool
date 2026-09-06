def remove_extras(lst):
    # Create a new list to store elements that haven't been seen yet
    result = []
    seen = set()
    for item in lst:
        if item not in seen:
            result.append(item)
            seen.add(item)
    return result