def sort_age(lst):
    newlst = []
    while lst:
        big = max(lst, key=lambda x: x[1])
        lst.remove(big)
        newlst.append(big)
    return newlst