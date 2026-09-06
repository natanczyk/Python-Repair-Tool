def remove_extras(lst):
    seen = []
    for num in lst:
        if num not in seen:
            seen.append(num)
    return seen