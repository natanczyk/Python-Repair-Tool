def search(x, seq):
    pos = len(seq)
    for i,elem in enumerate(seq):
        if elem>=x:
            if pos == len(seq):
                pos=i
            else:
                break
    return pos