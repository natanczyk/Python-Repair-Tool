def sort_age(lst):
    agelist = []
    for person in lst:
        inserted = False
        for i in range(len(agelist)):
            if person[1] >= agelist[i][1]:
                agelist.insert(i, person)
                inserted = True
                break
        if not inserted:
            agelist.append(person)
    return agelist