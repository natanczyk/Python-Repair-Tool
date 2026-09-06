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
            elif i < len(seq) - 1 and seq[i] < x < seq[i+1]:
                return i + 1
        return len(seq)