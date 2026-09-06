def remove_extras(lst):
    if not lst:
        return []
    seq = [lst[0]]
    for i in lst[1:]:
        if i not in seq:
            seq.append(i)
    return seq