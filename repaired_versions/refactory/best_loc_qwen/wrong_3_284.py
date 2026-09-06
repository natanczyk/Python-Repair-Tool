def remove_extras(lst):
    result = []
    for x in range(len(lst)):
        if lst[x] not in result:
            result.append(lst[x])
    return result