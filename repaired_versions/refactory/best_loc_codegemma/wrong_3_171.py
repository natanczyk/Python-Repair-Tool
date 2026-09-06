def remove_extras(lst):
    one = []
    for repeat in lst:
        if repeat not in one:
            one.append(repeat)
    return one