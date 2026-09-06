def search(x, seq):
    if not seq:  # Check if the sequence is empty
        return 0
    if x < seq[0]:
        indx = 0
    elif x > seq[-1]:
        indx = len(seq)  # Use len(seq) instead of seq.index(seq[-1]) + 1
    else:
        for i, val in enumerate(seq):
            if x <= val:
                indx = i
                break
    return indx