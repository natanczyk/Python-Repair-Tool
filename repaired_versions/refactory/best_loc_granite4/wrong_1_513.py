def search(x, seq):
    if not seq:  # Handle empty sequence
        return 0
    x = int(x)
    if x <= seq[0]:
        return 0
    if x > seq[-1]:
        return len(seq)
    for i in range(1, len(seq)):
        if x <= seq[i]:
            return i
    return len(seq)  # Fallback, should not reach here for valid input