def search(x,seq):
    if type(seq) == tuple:
        tup = ()
        for i in seq:
            if i < x:
                tup = tup + (i,)
        return len(tup)
        
    elif type(seq) == list:
        counter = 0
        for i in seq:
            if i < x:
                counter = counter + 1
        return counter