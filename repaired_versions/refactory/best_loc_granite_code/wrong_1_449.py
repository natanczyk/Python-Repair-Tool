def search(x, seq):
    for i in range(len(seq)):
        if x == seq[i]:
            return i
        elif x < seq[0]:
            return 0
        elif i < len(seq) - 1 and x > seq[i] and x < seq[i+1]:
            return i+1
    return len(seq)