def remove_extras(lst):
    l = len(lst)
    i = 0
    while i < l:
        j = i + 1
        while j < l:
            if lst[i] == lst[j]:
                del lst[j]
                l -= 1
            else:
                j += 1
        i += 1
    return lst