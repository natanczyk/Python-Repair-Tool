def remove_extras(lst):
    # Remove duplicates while preserving order
    seen = []
    for item in lst:
        if item not in seen:
            seen.append(item)
    return seen