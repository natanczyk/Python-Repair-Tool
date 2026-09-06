def search(x, seq):
    if not seq:  # Handle empty sequence
        return 0

    for i, val in enumerate(seq):
        if x <= val:
            return i
        if i == len(seq) - 1:  # If x is greater than all elements
            return len(seq)

    return len(seq)  # Fallback, though logically unreachable