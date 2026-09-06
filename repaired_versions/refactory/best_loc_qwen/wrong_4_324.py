def sort_age(lst):
    newnew = [lst[0]] if lst else []
    for i in lst[1:]:
        inserted = False
        for j in range(len(newnew)):
            if i[1] > newnew[j][1]:
                newnew.insert(j, i)
                inserted = True
                break
            elif i[1] < newnew[j][1]:
                continue
        if not inserted:
            newnew.append(i)
    return newnew