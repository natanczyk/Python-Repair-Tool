def remove_extras(lst):
    check = True
    lst1 = []
    for i in lst:
        check = True  # Reset check at the start of each iteration
        for j in lst1:
            if j == i:
                check = False
        if check:
            lst1.append(i)
    return lst1