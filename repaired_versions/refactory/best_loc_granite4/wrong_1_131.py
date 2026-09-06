def search(x, seq):
    if not seq:  # Check if the sequence is empty
        return 0
    elif x <= seq[0]:
        return 0
    else:
        for i in range(len(seq) - 1):
            if seq[i] < x <= seq[i + 1]:
                return i + 1
        return len(seq)