def search(x, seq):
    if type(seq) == tuple:
        tup = ()
        for i in seq:
            if i < x:
                tup = tup + (i,)
            else:
                break
        return len(tup)
        
    elif type(seq) == list:
        counter = 0
        for i in seq:
            if i < x:
                counter += 1
        return counter