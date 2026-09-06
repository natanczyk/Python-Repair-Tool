def search(x, seq):
    if len(seq) == 0:
        return len(seq)
    else:     
        for i in range(len(seq)):
            if x <= seq[i]:
                return i
        return len(seq)