def remove_extras(lst):
    seen = []
    for ele in lst:
        if ele not in seen:
            seen.append(ele)
    return seen