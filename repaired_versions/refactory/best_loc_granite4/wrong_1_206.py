def search(x, seq):
    if not seq:  # Handle empty sequence
        return 0
    if x < seq[0]:
        return 0
    elif x > seq[-1]:
        return len(seq)
    else:
        for i in range(len(seq)):
            if x <= seq[i]:
                return i