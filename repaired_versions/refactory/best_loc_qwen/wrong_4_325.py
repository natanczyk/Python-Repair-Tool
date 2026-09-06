def sort_age(lst):
    newnew = []
    for i in lst:
        inserted = False
        for j in range(len(newnew)):
            if i[1] >= newnew[j][1]:
                newnew.insert(j, i)
                inserted = True
                break
            elif i[1] < newnew[j][1]:
                continue
        if not inserted:
            newnew.append(i)
    return newnew