def search(x, seq):
    if not seq:
        return 0
    elif x < seq[0]:
        return 0
    elif x > seq[-1]:
        return len(seq)
    else:
        product = -1
        for i in range(len(seq)):
            if x == seq[i]:
                return i
            elif x > seq[i] and (i+1 == len(seq) or x < seq[i+1]):
                return i + 1
        return product