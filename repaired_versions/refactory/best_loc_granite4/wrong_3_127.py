def remove_extras(lst):
    if not lst:  # Check if the list is empty
        return []
    seq = [lst[0],]
    for i in lst:
        if i not in seq:
            seq = seq + [i,]
    return seq