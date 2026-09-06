def search(x, seq):
    if not seq:  # Check if the sequence is empty
        return 0
    for i, elem in enumerate(seq):
        if x <= elem:
            return i
        elif i == (len(seq) - 1):
            return i + 1