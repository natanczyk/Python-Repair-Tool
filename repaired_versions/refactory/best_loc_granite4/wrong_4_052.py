def sort_age(lst):
    newlst = []
    while lst:
        oldest = max(lst, key=lambda person: person[1])
        newlst.append(oldest)
        lst.remove(oldest)
    return newlst