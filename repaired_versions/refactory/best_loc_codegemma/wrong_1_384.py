def search(x, seq):
    for i in range(len(seq)):
        if seq[i] < x:
            continue
        elif seq[i] >= x:
            if i == 0 or seq[i-1] < x:
                return i
            else:
                return i-1
    return len(seq)