def search(x, seq):
    if not seq:  # Check if the sequence is empty
        return 0
    for i in range(len(seq)):
        if x <= seq[i]:
            return i
    return len(seq)  # Return the length if x is greater than all elements