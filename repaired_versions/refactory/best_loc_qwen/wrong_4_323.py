def sort_age(lst):
    if not lst:
        return []
    
    new_lst = lst[:]
    newnew = [new_lst[0]]
    for i in new_lst[1:]:
        inserted = False
        for j in range(len(newnew)):
            if i[1] >= newnew[j][1]:
                newnew.insert(j, i)
                inserted = True
                break
        if not inserted:
            newnew.append(i)
    return newnew