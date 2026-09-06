def search(x, seq):
    if not seq:  # Handle empty sequences
        return 0
    for i, elem in enumerate(seq):
        if elem is None:
            return 0
        elif x <= elem:
            return i
        elif i == (len(seq) - 1):
            return i + 1