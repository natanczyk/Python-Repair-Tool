def remove_extras(lst):
    result = []
    seen = set()
    for i in lst:
        if i not in seen:
            result.append(i)
            seen.add(i)
    return result