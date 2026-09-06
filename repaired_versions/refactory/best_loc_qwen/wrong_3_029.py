def remove_extras(lst):
    result = []
    for i in lst:
        if i not in result:
            result.append(i)
    return result

def remove_multiple(n, lst):
    if lst.count(n) == 1:
        return lst
    else:
        lst.reverse()
        lst.remove(n)
        lst.reverse()
        return remove_multiple(n, lst)