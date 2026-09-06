def remove_extras(lst):
    """
    Returns a new list with all repeated occurrences of any element removed,
    preserving the original order of first occurrences.
    """
    result = []
    seen = set()
    for item in lst:
        if item not in seen:
            result.append(item)
            seen.add(item)
    return result