def remove_extras(lst):
    # Create a copy to avoid mutating the original list if desired, 
    # though the task asks for a new list.
    result = []
    for item in lst:
        if item not in result:
            result.append(item)
    return result