def search(x, seq):
    if not seq:  # Check if the sequence is empty (handles both empty list and empty tuple)
        return 0
    for i, elem in enumerate(seq):
        if elem >= x:
            return i
    return len(seq)