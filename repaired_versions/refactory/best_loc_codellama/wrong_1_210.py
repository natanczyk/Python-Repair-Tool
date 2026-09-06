def search(x, seq):
    if len(seq) == 0:
        return 0
    if x < seq[0]:
        return 0
    elif x > seq[-1]:
        return len(seq)
    else:
        for i in range(len(seq)):
            if seq[i] == x:
                return i
            elif seq[i] < x < seq[i+1]:
                return i+1
        return len(seq)