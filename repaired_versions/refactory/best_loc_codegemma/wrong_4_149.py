def sort_age(lst):
    new = []
    while lst:
        big = lst[0][1]
        name =lst[0][0]
        for ele in lst:
            if ele[1]>big:
                big = ele[1]
                name = ele[0]
        new.append((name,big))
        lst.remove((name,big))
    return new