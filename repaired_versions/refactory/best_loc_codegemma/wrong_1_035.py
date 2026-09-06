def search(x, seq):
    if not seq:
        return 0
    for i in range(len(seq)):
        if x == seq[i]:
            return i
        elif x < seq[i]:
            return i
        elif i == len(seq)-1 and x >= seq[i]:
            return i+1
        elif seq[i] < x < seq[i+1]:
            return i+1