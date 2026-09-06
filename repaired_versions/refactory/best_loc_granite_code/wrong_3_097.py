def remove_extras(lst):
    copy = lst.copy()
    for i in copy:
        if lst.count(i) > 1:
            left = lst[:lst.index(i)+1]
            right = lst[lst.index(i)+1:]
            right.remove(i)
            lst = left + right
    return lst