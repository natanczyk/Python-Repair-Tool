def search(x, seq):
    for i, elem in enumerate(seq):
        if x < elem: 
            return i
        elif x == elem:
            return i
    if seq == []:
        return 0
    else:
        return len(seq)