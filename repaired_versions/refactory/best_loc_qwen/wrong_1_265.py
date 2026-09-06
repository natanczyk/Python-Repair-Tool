def search(x, seq):
    if seq == [] or seq == ():
        return 0
    if seq[0] >= x:
        return 0
    if seq[len(seq)-1] < x:
        return len(seq)
    else:
        for i in range(len(seq)):
            if seq[i] >= x:
                return i
                break