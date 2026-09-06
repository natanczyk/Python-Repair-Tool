def remove_extras(lst):
    new = []
    for ele in lst:
        if ele not in new:
            new.append(ele)
    return new