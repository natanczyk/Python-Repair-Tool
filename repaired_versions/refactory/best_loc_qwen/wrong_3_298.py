def remove_extras(lst):
    new = []
    for x in range(len(lst)):
        if lst[x] not in new:
            new.append(lst[x])
    return new