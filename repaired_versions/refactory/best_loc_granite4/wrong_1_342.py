def search(x, seq):
    if not seq:  # Check if the sequence is empty
        return 0
    for i, value in enumerate(seq):
        if x == value:
            return i
        if x < value:  # If x is less than the current value, it should be inserted here
            return i
    return len(seq)  # If x is greater than all elements, return the length of the sequence