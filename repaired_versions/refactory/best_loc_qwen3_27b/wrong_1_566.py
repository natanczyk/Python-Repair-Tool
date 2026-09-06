def search(x, seq):
    if not seq:
        return 0
    for i, elem in enumerate(seq):
        if elem == None:
            return 0
        elif x <= elem:
            return i
        elif i == (len(seq)-1):
            return i+1
        else:
            continue
    return len(seq)