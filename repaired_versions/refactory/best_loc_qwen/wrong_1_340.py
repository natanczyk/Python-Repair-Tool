def search(x, seq):
    counter = 0
    for counter in range(len(seq)):
        if x <= seq[counter]:
            return counter
    return len(seq)