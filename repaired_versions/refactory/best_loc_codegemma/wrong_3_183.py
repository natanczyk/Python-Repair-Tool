def remove_extras(lst):
    seen = set()
    unique = []
    for e in lst:
        if e not in seen:
            unique.append(e)
            seen.add(e)
    return unique