def search(x, seq):
    if type(seq) == tuple:
        tup = ()
        for i in seq:
            if i < x:
                tup = tup + (i,)
            else:
                tup = tup + (x,)
                break
        else:
            return len(tup)
        return len(tup) - 1
        
    elif type(seq) == list:
        lst = []
        for i in seq:
            if i < x:
                lst.append(i)
            else:
                lst.append(x)
                break
        else:
            return len(lst)
        return len(lst) - 1