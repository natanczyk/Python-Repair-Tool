def search(x, seq):
    # Handle empty sequence case
    if not seq:
        return 0
    
    for i, elem in enumerate(seq):
        if x < seq[-1]:
            if x > elem:
                continue
            elif x < elem and type(seq) == tuple:
                seq = seq[:i] + (x,) + seq[i:]
            elif x < elem and type(seq) == list:
                seq = seq[:i] + [x,] + seq[i:]
            return seq.index(x)
        elif x > seq[-1]:
            if type(seq) == tuple:
                seq += (x,)
            elif type(seq) == list:
                seq += [x,]
            return seq.index(x)
    
    # If x equals the last element, it's already in the sequence
    return seq.index(x)