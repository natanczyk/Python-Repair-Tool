def sort_age(lst):
    newlst=[]
    while lst:
        oldest = lst[0] #first person
        for person in lst:
            if person[1]>oldest[1]:
                oldest=person
        newlst.append(oldest)
        lst.remove(oldest)
    return newlst