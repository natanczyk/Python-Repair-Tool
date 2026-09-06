def remove_extras(lst):
    lst1 = lst.copy()
    seen = set()
    result = []
    for i in lst1:
        if i not in seen:
            result.append(i)
            seen.add(i)
    return result