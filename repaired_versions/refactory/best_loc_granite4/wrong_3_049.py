def remove_extras(lst):
    seen = set()
    new = []
    for x in lst:
        if x not in seen:
            new.append(x)
            seen.add(x)
    return new