def search(x, seq):
    for i in range(len(seq)):
        if x <= seq[i]:
            return seq.index(seq[i])
    return seq.index(seq[-1])+1 if seq else 0