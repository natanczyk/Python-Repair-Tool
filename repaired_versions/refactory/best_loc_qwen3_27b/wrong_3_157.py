def remove_extras(lst):
    seen = []
    for item in lst:
        if item not in seen:
            seen.append(item)
    return seen