def remove_extras(lst):
    result = []
    seen = set()
    for i in lst:
        if i not in seen:
            seen.add(i)
            result.append(i)
    return result