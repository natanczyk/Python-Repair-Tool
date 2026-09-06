def remove_extras(lst):
    for i in reversed(range(len(lst))):
        if lst[i] in lst[:i]:
            lst.pop(i)
    return lst