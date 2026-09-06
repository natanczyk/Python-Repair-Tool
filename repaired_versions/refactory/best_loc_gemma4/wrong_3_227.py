def remove_extras(lst):
    seen = set()
    result = []
    for i in lst:
        if i not in seen:
            result.append(i)
            seen.add(i)
    return result