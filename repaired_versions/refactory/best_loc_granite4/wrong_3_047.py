def remove_extras(lst):
    new = []
    seen = set()
    for x in lst:
        if x not in seen:
            new.append(x)
            seen.add(x)
    return new