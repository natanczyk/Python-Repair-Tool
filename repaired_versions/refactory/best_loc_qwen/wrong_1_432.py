def search(x, seq):
    if type(seq) == tuple:
        for i in range(len(seq)):
            if x <= seq[i]:
                return i
        return len(seq)
    elif type(seq) == list:
        for i in range(len(seq)):
            if x <= seq[i]:
                return i
        return len(seq)

    # Handle empty sequences
    return 0