def sort_age(lst):
    if not lst:
        return []
    
    agelist = [lst[0],]
    for i in lst[1:]:
        inserted = False
        for x in range(len(agelist)):
            if i[1] >= agelist[x][1]:
                agelist.insert(x, i)
                inserted = True
                break
        if not inserted:
            agelist.append(i)
    return agelist