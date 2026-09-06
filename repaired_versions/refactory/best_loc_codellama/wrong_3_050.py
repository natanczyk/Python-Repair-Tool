def remove_extras(lst):
    seen = set()
    result = []
    for ele in lst:
        if ele not in seen:
            result.append(ele)
            seen.add(ele)
    return result