def remove_extras(lst):
    # Create a new list to preserve order and avoid modifying the original list during iteration
    seen = []
    for item in lst:
        if item not in seen:
            seen.append(item)
    return seen