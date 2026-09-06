def remove_extras(lst):
    n = len(lst)
    result = []
    seen = set()
    for i in range(n):
        if lst[i] not in seen:
            result.append(lst[i])
            seen.add(lst[i])
    return result