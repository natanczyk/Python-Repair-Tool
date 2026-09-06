def search(x, seq):
    if not seq:  # Check if seq is empty
        return 0
    elif x <= seq[0]:
        return 0
    elif x > seq[-1]:
        return len(seq)
    else:
        for i in range(len(seq) - 1):
            if seq[i] <= x <= seq[i + 1]:
                return i + 1