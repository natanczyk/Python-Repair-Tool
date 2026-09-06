def remove_extras(lst):
    l = len(lst)
    result = []
    for i in range(l):
        if lst[i] not in result:
            result.append(lst[i])
    return result