def remove_extras(lst):
    # To maintain the original order and remove duplicates, 
    # we iterate through the list and keep track of seen elements.
    seen = set()
    result = []
    for item in lst:
        if item not in seen:
            result.append(item)
            seen.add(item)
    return result