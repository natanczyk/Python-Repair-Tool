def search(x, seq):
    if not seq:
        return 0
    if x <= seq[0]:
        return 0
    elif x > seq[len(seq)-1]:
        return len(seq)
    else:
        for i, elem in enumerate(seq):
            if i + 1 < len(seq) and elem < x <= seq[i+1]:
                return i+1
            elif x == elem:
                return i
        return len(seq)