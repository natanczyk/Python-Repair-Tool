def search(x,seq):
    if type(seq) == tuple:
        tup = ()
        for i in seq:
            if i < x:
                tup = tup + (i,)
            else:
                tup = tup + (x,)
                break
        else:
            # If the loop completes without breaking, x is greater than all elements
            tup = tup + (x,)
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
            # If the loop completes without breaking, x is greater than all elements
            lst.append(x)
        return len(lst) - 1