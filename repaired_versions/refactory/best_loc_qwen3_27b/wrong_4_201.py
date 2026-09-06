def sort_age(lst):
    if not lst:
        return []
    
    agelist = [lst[0]]
    for i in lst[1:]:
        if i[1] > agelist[0][1]:
            agelist.insert(0, i)
        elif i[1] < agelist[-1][1]:
            agelist.append(i)
        else:
            for x in range(len(agelist) - 1):
                if agelist[x][1] > i[1] > agelist[x + 1][1]:
                    agelist.insert(x + 1, i)
                    break
    return agelist