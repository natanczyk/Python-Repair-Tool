def search(x, seq):
    if seq == []:
        return 0
    else:
        for i, elem in enumerate(seq):
            if x <= elem:
                return i
        return len(seq)