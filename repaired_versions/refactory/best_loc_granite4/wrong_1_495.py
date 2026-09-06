def search(x, seq):
    if not seq:  # Check if the sequence is empty
        return 0
    else:
        for i, elem in enumerate(seq):
            if x <= elem:
                return i
        return len(seq)  # Return len(seq) if x is greater than all elements