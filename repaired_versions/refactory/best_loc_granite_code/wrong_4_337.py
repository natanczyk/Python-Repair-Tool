def sort_age(lst):
    new_lst = []
    for x in lst:
        inserted = False
        for i, y in enumerate(new_lst):
            if x[1] > y[1]:
                new_lst.insert(i, x)
                inserted = True
                break
        if not inserted:
            new_lst.append(x)
    return new_lst