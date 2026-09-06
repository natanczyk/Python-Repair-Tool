def search(x, seq):
    if seq == []:
        return 0
    elif len(seq) == 1:
        if seq[0] < x:
            return 1
        else:
            return 0
    else:
        for i in range(len(seq)):
            if x == seq[i]:
                return i
            elif x > seq[i]:
                continue
            else:
                return i
        return len(seq)