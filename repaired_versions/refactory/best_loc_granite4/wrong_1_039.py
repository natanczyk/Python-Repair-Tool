def search(x, seq):
    if not seq:  # Handle empty sequence
        return 0

    for i, value in enumerate(seq):
        if x <= value:  # Include equality to handle exact matches
            return i

    return len(seq)  # If x is greater than all elements