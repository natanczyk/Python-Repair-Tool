def search(x, seq):
    if seq == ():
        return 0
    elif seq == []:
        return 0
    else:
        for i, elem in enumerate(seq):
            if x <= elem:
                return i
            elif x > max(seq):
                return len(seq)
        return len(seq)