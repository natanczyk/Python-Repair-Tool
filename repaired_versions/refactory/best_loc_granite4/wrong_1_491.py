def search(x, seq):
    l = len(seq)
    i = 0  # Initialize i to handle empty sequences
    for i in range(l):
        if x <= seq[i]:
            break
    if l > 0 and x > seq[l - 1]:
        i = l
    return i