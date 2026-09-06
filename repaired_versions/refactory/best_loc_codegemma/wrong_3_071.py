def remove_extras(lst):
    """
    This function takes in a list and returns a new list with all repeated occurrences of any element removed.
    For example, remove_extras([5, 2, 1, 2, 3]) returns the list [5, 2, 1, 3].
    """
    seen = set()
    result = []
    for element in lst:
        if element not in seen:
            seen.add(element)
            result.append(element)
    return result