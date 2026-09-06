def remove_extras(lst):
    pst=[]
    for i in lst:
        if i not in pst:
            pst.append(i)
    return pst