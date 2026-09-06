def remove_extras(lst):
    length = len(lst)
    result = []
    for i in range(length):
        if lst[i] not in result:
            result.append(lst[i])
    return result