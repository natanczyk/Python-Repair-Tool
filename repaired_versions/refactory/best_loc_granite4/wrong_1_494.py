def search(x, seq):
    if not seq:  # Check if the sequence is empty (handles both () and [])
        return 0
    for i, elem in enumerate(seq):
        if x <= elem:
            return i
    return len(seq)