def search(x, seq):
    if not seq:  # Check if the sequence is empty
        return 0
    if x <= seq[0]:
        return 0
    for i in range(len(seq) - 1):  # Iterate only up to the second-to-last element
        if seq[i] < x <= seq[i+1]:
            return i+1
    return len(seq)