def search(x, seq):
    if not seq:  # Handles both empty lists and empty tuples
        return 0
    for i, elem in enumerate(seq):
        if x <= elem:
            return i
    return len(seq)  # Return the length of the sequence if no element satisfies the condition