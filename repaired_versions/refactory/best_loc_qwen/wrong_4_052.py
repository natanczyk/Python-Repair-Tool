def sort_age(lst):
    newlst = []
    while lst:
        oldest = lst[0][1]  # first age
        oldest_person = lst[0]
        for person in lst:
            if person[1] > oldest:
                oldest = person[1]
                oldest_person = person
        newlst.append(oldest_person)
        lst.remove(oldest_person)
    return newlst