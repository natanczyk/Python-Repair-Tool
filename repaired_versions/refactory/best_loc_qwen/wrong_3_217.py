def remove_extras(lst):
    new = []
    seen = set()
    for ele in lst:
        if ele not in seen:
            new.append(ele)
            seen.add(ele)
    return new