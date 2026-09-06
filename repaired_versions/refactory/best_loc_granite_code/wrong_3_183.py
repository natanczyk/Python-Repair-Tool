def remove_extras(lst):
    removed = []
    seen = set()
    for e in lst:
        if e not in seen:
            removed.append(e)
            seen.add(e)
    return removed