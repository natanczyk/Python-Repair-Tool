def remove_extras(lst):
    new = []
    for x in lst:
        if lst.count(x) == 1:
            new.append(x)
        elif x not in new:
            new.append(x)
    return new