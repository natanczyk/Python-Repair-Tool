def search(x, seq):
    if not seq: 
        return 0
    elif len(seq) == 1:
        if seq[0] < x:
            return 1
        else: 
            return 0
    elif seq[-1] < x:
        return len(seq)
    else:
        for i in range(len(seq)):
            if x <= seq[i]:
                return i
        return len(seq)