def remove_extras(lst):
    # your code here
    result = []
    for item in lst:
        if item in result:
            continue
        else:
            result.append(item)
    return result