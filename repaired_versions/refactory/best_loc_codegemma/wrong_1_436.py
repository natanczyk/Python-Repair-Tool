def search(x,seq):
    tup = ()
    if type(seq) == tuple:
        for i in seq:
            if i < x:
                tup = tup + (i,)
            elif i >= x:
                break
        return len(tup)
    else:
        for i in seq:
            if i < x:
                tup = tup + (i,)
            elif i >= x:
                break
        return len(tup)