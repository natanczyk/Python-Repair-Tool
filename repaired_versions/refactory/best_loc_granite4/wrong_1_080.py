def search(x, seq):
    if not seq:  # Check if seq is empty (handles both empty lists and empty tuples)
        return 0
    for count, ele in enumerate(seq):
        if x <= ele:
            return count
    return len(seq)  # If no element is greater than x, return the length of the sequence