def remove_extras(lst):
    # Create a new list to store elements that haven't been seen yet
    result = []
    for item in lst:
        if item not in result:
            result.append(item)
    return result