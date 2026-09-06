def remove_extras(lst):
    seen = []
    for i in lst:
        if i not in seen:
            seen.append(i)
    return seen
    


    






def remove_multiple(n, lst):
    if lst.count(n) == 1:
        return lst
    else:
        lst.reverse()
        lst.remove(n)
        lst.reverse()
        return remove_multiple(n, lst)