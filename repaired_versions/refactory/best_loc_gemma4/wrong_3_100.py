def remove_extras(lst):
    # To remove duplicates while preserving the original order of first occurrences,
    # we iterate through the list and keep track of elements we have already seen.
    seen = set()
    result = []
    for item in lst:
        if item not in seen:
            result.append(item)
            seen.add(item)
    return result