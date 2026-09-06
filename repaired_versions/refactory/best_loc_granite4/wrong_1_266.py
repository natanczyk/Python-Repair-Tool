def search(x, seq):
    if not seq or seq[0] >= x:
        return 0
    elif seq[-1] < x:
        return len(seq)
    else:
        for i in range(len(seq) - 1):
            if seq[i] < x and seq[i + 1] >= x:
                return i + 1