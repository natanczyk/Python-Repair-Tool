def remove_extras(lst):
    # Initialize an empty list to store unique elements
    result = []
    for item in lst:
        # Check if the item is already in the result list
        if item not in result:
            # If not present, add it to the result list
            result.append(item)
    return result