def remove_extras(lst):
    copy = lst.copy()
    result = []
    for i in copy:
        if i not in result:
            result.append(i)
    return result