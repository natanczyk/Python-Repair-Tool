def search(x, seq):
    if not seq:
        return 0
    if x < seq[0]:
        return 0
    if x > seq[-1]:
        return len(seq)
    for i in range(len(seq) - 1):
        if seq[i] < x <= seq[i + 1]:
            return i + 1
    # Handle case where x is equal to an element in the sequence
    for i, val in enumerate(seq):
        if x == val:
            return i
    return len(seq)  # Fallback, should not reach here for valid input