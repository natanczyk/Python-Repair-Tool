def remove_extras(lst):
    """
    This function removes all repeated occurrences of any element in a list.

    Args:
        lst: The input list.

    Returns:
        A new list with all repeated occurrences of any element removed.
    """
    seen = set()
    result = []
    for element in lst:
        if element not in seen:
            seen.add(element)
            result.append(element)
    return result