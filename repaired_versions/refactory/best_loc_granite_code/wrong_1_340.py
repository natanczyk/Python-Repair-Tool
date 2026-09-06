def search(x, seq):
    for counter in range(len(seq)):
        if x <= seq[counter]:
            return counter
    return len(seq)