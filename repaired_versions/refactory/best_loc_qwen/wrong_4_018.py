def sort_age(lst):
    if not lst:
        return []
    newlst = []
    for i in lst:
        if len(newlst) == 0:
            newlst.append(i)
        else:
            for j in range(len(newlst)):
                if i[1] > newlst[j][1]:
                    newlst.insert(j, i)
                    break
                elif j == len(newlst) - 1:
                    newlst.append(i)
    return newlst