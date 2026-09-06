def remove_extras(lst):
    seen = set()
    result = []
    for e in lst:
        if e not in seen:
            seen.add(e)
            result.append(e)
    return result