def remove_extras(lst):
    result = []
    for num in lst:
        if num not in result:
            result.append(num)
    return result