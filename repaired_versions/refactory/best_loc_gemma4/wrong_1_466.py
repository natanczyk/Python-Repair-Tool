def search(x, seq):
    if not seq:
        return 0
    elif x < seq[0]:
        return 0
    elif x > seq[len(seq)-1]:
        return len(seq)
    else:
        for i in range(len(seq)):
            if x == seq[i]:
                return i
            elif x < seq[i]:
                return i
        return len(seq)