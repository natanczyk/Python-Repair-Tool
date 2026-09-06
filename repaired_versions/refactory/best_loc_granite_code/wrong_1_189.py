def search(x, seq):
    if seq == []:
        return 0
    elif x < 0:
        return 0
    elif x <= seq[0]:
        return 0
    elif x > max(seq):
        return len(seq)
    else:
        for i in range(len(seq) - 1):
            if (x > seq[i]) and (x <= seq[i + 1]):
                return i + 1