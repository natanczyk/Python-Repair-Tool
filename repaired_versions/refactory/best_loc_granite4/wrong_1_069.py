def search(x, seq):
    if not seq:  # Check if the sequence is empty
        return 0
    for i, elem in enumerate(seq):
        if x == elem:
            return i
        elif x < elem:
            return i
    return len(seq)  # x is greater than all elements