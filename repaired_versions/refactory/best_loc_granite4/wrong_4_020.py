def sort_age(lst):
    if not lst:
        return []
    
    new_lst = [lst[0]]
    for i in lst[1:]:
        inserted = False
        for j in range(len(new_lst)):
            if i[1] > new_lst[j][1]:
                new_lst.insert(j, i)
                inserted = True
                break
        if not inserted:
            new_lst.append(i)
    
    return new_lst