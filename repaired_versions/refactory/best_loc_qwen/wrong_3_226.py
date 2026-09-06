def remove_extras(lst):
    result = []
    seen = set()
    for num in lst:
        if num not in seen:
            result.append(num)
            seen.add(num)
    return result