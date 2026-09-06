def search(x, seq):
    if not seq:  # Check for empty sequence first
        return 0
    if x < seq[0]:
        return 0
    if x > seq[-1]:
        return len(seq)
    for i in range(len(seq)):
        if x <= seq[i]:
            return i
    return len(seq)  # Fallback, should not reach here for valid input