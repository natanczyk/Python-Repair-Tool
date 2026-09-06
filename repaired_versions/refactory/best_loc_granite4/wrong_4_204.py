def sort_age(lst):
    if not lst:
        return []
    agelist = [lst[0],]
    for i in range(1, len(lst)):
        if lst[i][1] > agelist[0][1]:
            agelist.insert(0, lst[i])
        elif lst[i][1] < agelist[-1][1]:
            agelist.append(lst[i])
        else:
            for x in range(len(agelist) - 1):
                if agelist[x][1] > lst[i][1] > agelist[x + 1][1]:
                    agelist.insert(x + 1, lst[i])
                    break
    return agelist