def sort_age(lst):
    agelist = []
    for i in range(len(lst)):
        if lst[i][1] > agelist[0][1] if agelist else lst[i][1]:
            agelist.insert(0, lst[i])
        elif lst[i][1] < agelist[-1][1] if agelist else lst[i][1]:
            agelist.insert(len(agelist), lst[i])
        else:
            for x in range(len(agelist)):
                if agelist[x][1] > lst[i][1] > agelist[x + 1][1]:
                    agelist.insert(x + 1, lst[i])
                    break
    return agelist