def remove_extras(lst):
    result = []
    seen = set()
    for ele in lst:
        if ele not in seen:
            result.append(ele)
            seen.add(ele)
    return result