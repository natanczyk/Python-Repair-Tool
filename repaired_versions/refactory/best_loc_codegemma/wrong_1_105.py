def search(x, seq):
    for i in range(len(seq)):
        if x > seq[i]:
            continue
        elif x <= seq[i]:
            if i == 0 or x > seq[i-1]:
                return i
    return len(seq)