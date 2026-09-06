def search(x, seq):
    if len(seq) == 0:
        return 0
    # Check if x is less than or equal to the first element
    if x <= seq[0]:
        return 0
    # Search for the position where x fits in the sequence
    for i in range(len(seq) - 1):
        if seq[i] < x <= seq[i + 1]:
            return i + 1
    # If x is greater than the last element, return len(seq)
    # If x equals the last element, it should return the index of the last element
    if x > seq[-1]:
        return len(seq)
    else:
        # x == seq[-1], so it belongs at the last position
        return len(seq) - 1