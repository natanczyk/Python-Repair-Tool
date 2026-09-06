def search(x, seq):
    if not seq:  # Check if the sequence is empty (handles both list and tuple)
        return 0
    for i, elem in enumerate(seq):
        if elem >= x:
            return i
    return len(seq)  # If no element is >= x, return the position after the last element