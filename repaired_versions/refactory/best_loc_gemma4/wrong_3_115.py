def remove_extras(lst):
    # To remove duplicates while preserving order, we track seen elements
    seen = set()
    result = []
    for item in lst:
        if item not in seen:
            result.append(item)
            seen.add(item)
    return result