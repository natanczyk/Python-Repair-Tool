def search(x, seq):
    for i in range(len(seq)):
        if x < seq[i]:
            return i
        elif x == seq[i]:
            return i
        elif i == len(seq)-1 or x <= seq[i+1]:
            return i+1
    return len(seq)