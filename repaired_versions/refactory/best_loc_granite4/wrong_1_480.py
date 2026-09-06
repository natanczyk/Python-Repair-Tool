def search(x, seq):
    if not seq:  # Handle empty sequence
        return 0
    for i, elem in enumerate(seq):
        if x <= elem:  # Include equality in the condition
            return i
    return len(seq)  # Return length if x is greater than all elements