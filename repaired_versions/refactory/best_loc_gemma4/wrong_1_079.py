def search(x, seq):
    if not seq:
        return 0
    for count, ele in enumerate(seq):
        if x <= ele:
            return count
    
    # If the loop finishes without returning, it means x is greater than all elements.
    # The original logic intended to return len(seq) in this case.
    return len(seq)