def remove_extras(lst):
    seen = set()
    result = []
    for num in lst:
        if num not in seen:
            result.append(num)
            seen.add(num)
    return result