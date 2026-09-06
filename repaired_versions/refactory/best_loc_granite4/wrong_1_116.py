def search(x, seq):
    if not seq:  # Check for empty sequence (list or tuple)
        return 0
    for i, currentvalue in enumerate(seq):
        if x <= currentvalue:
            return i
    return len(seq)