def search(x, seq):
    for i in range(len(seq)):
        if x < seq[i]:
            return i
        elif x == seq[i]:
            return i
        elif i == len(seq)-1 and x > seq[i]:
            return i+1
    return 0