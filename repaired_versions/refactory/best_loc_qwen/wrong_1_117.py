def search(x, seq):
    if not seq:  # Check if seq is empty
        return 0
    if x > seq[-1]:  # Correct the condition to handle the last element properly
        return len(seq)
    else:
        for i, elem in enumerate(seq):
            if elem >= x:
                return i
    return 0  # This line is redundant due to the loop, but kept for completeness