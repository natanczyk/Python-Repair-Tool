def remove_extras(lst, seen=None):
    if seen is None:
        seen = set()
    if not lst:
        return []
    if lst[0] in seen:
        return remove_extras(lst[1:], seen)
    else:
        seen.add(lst[0])
        return [lst[0]] + remove_extras(lst[1:], seen)