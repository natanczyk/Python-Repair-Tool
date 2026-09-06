def remove_extras(lst):
    seen = []
    for i in lst:
        if i not in seen:
            seen.append(i)
    return seen