def search(x, seq):
    if not seq:  # Check if the sequence is empty
        return 0
    max_val = max(seq)  # Compute the maximum value once before the loop
    for i in range(len(seq)):
        if x <= seq[i]:
            return i
    return len(seq)  # Return the length if x is greater than all elements