def remove_extras(lst):
    # your code here
    result = []
    for item in lst:
        if item not in result:
            result.append(item)
    return result