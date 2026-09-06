def remove_extras(lst):
    result = []
    for k in range(len(lst)):
        if lst[k] not in result:
            result.append(lst[k])
    return result