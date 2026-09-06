def remove_extras(lst):
    i = len(lst) - 1
    while i >= 0:
        if lst[i] in lst[:i]:
            lst.pop(i)
        i = i - 1
    return lst