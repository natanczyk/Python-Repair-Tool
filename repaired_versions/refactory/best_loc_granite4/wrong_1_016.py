def search(x, seq):
    if not seq:  # Handle empty sequence
        return 0
    if x < seq[0]:
        return 0
    elif x > seq[-1]:
        return len(seq)
    for i, elem in enumerate(seq):
        if elem >= x:  # Find the first element greater than or equal to x
            return i