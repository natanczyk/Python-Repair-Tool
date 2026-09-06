def search(x, seq):
    if not seq:  # Check for empty sequence first
        return 0

    for i in range(len(seq)):
        if x <= seq[i]:
            return i
    return len(seq)  # Return length if x is greater than all elements