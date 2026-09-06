def search(x, seq):
    if not seq:  # Handle empty sequence
        return 0
    for index, element in enumerate(seq):
        if x <= element:
            return index
    # If x is greater than all elements, return the length of the sequence
    return len(seq)