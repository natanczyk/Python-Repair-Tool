def search(x, seq):
    if seq == [] or seq == ():
        return 0
    if x <= seq[0]:
        return 0
    elif x > seq[-1]:
        return len(seq)
    else:
        for i, elem in enumerate(seq[:-1]):
            if elem <= x <= seq[i+1]:
                return i+1