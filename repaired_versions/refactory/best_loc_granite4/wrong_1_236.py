def search(x, seq):
    if not seq:  # Check if the sequence is empty
        return 0
    if x < seq[0]:
        return 0
    elif x > seq[-1]:
        return len(seq)
    else:
        for i, value in enumerate(seq):
            if x > value:
                continue
            else:
                return i