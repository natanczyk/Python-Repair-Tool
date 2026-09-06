def remove_extras(lst):
    for i in reversed(range(len(lst))):
        num = lst[i]
        if lst.count(num) > 1:
            lst.pop(i)
    return lst