def remove_extras(lst):
    seq = []
    for i in lst:
        if i not in seq:
            seq.append(i)
    return seq