def remove_extras(lst):
    extra = []
    for i in lst:
        if i not in extra:
            extra.append(i)
    return extra