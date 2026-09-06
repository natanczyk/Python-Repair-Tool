def search(x, seq):
    if not seq:  # Handles both empty lists and empty tuples
        return 0
    for a, b in enumerate(seq):
        if x <= b:
            return a
    return len(seq)  # Return the length of seq if x is greater than all elements