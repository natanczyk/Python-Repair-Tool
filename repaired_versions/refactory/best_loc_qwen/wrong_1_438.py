def search(x, seq):
    if type(seq) == tuple:
        tup = ()
        for i in seq:
            if i < x:
                tup = tup + (i,)
            else:
                return len(tup)
        return len(tup)
        
    elif type(seq) == list:
        lst = []
        for i in seq:
            if i < x:
                lst.append(i)
            else:
                return len(lst)
        return len(lst)