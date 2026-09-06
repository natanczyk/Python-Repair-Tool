def remove_extras(lst):
    a = []
    for repeat in lst:
        if repeat not in a:
            a.append(repeat)
    return a