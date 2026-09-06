def sort_age(lst):
    if not lst:
        return []
    
    agelist = [lst[0],]
    for i in range(1, len(lst)):
        current_person = lst[i]
        inserted = False
        for x in range(len(agelist)):
            if current_person[1] >= agelist[x][1]:
                agelist.insert(x, current_person)
                inserted = True
                break
        if not inserted:
            agelist.append(current_person)
    return agelist