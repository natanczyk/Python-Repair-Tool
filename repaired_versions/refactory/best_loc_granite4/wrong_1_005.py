def search(x, seq):
    if not seq:  # Check if the sequence is empty
        return 0
    for i, value in enumerate(seq):
        if x <= value:  # Find the first position where x can be inserted
            return i
    return len(seq)  # If x is greater than all elements, insert at the end