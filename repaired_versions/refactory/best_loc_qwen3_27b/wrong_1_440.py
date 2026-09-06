def search(x,seq):
    if type(seq) == tuple:
        counter = 0
        for i in seq:
            if i < x:
                counter = counter + 1
        return counter
        
    elif type(seq) == list:
        counter = 0
        for i in seq:
            if i < x:
                counter = counter + 1
        return counter