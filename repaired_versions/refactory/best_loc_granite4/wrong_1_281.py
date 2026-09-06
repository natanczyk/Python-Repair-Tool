def search(x, seq):
    if not seq:  # Check if the sequence is empty
        return 0
    if x <= seq[0]:  # If x is less than or equal to the first element
        return 0
    for i in range(len(seq) - 1):
        if seq[i] < x <= seq[i + 1]:
            return i + 1
    if x > seq[-1]:  # If x is greater than the last element
        return len(seq)
    return 0  # If x is equal to an element in the sequence