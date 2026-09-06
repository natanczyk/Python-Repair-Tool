def search(x, seq):
    if type(seq) == tuple:
        count = 0
        for i in seq:
            if i < x:
                count += 1
            else:
                break
        return count
        
    elif type(seq) == list:
        counter = 0
        for i in seq:
            if i < x:
                counter += 1
        return counter