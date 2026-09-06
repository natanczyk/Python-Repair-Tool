def search(x, seq):
    position = len(seq)
    for i in range(len(seq)):
        if x <= seq[i] and (i == 0 or x > seq[i-1]):
            position = i
            break
    return position