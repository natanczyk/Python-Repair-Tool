def remove_extras(lst):
    n = len(lst)
    seen = set()
    result = []
    for i in range(n):
        if lst[i] not in seen:
            seen.add(lst[i])
            result.append(lst[i])
    return result