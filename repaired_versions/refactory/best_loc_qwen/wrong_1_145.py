def search(x, seq):
    n = []
    seq = list(seq)
    
    for i in seq:
        if i < x:
            n.append(i)
        elif i == x:
            n.append(i)
            n.append(x)
            break
        else:
            n.append(x)
            break
    
    count = list(enumerate(n))
    
    for b in count:
        if b[1] == x:
            return b[0]
    
    return len(count)