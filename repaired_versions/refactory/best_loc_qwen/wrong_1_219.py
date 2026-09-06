def search(x, seq):
    if not seq:  # Check if the sequence is empty
        return 0
    for i, elem in enumerate(seq):
        if x <= elem:
            return i
    return len(seq)  # Handle the case when x is greater than all elements in the sequence