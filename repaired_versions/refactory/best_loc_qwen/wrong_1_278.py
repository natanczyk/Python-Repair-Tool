def search(x, seq):
    if not seq:  # Check if the sequence is empty
        return 0
    if x > seq[-1]:
        return len(seq)
    else:
        for i, elem in enumerate(seq):
            if x <= elem:
                return i
            else:
                continue