def search(x, seq):
    if not seq:  # Check if the sequence is empty (handles both empty list and empty tuple)
        return 0
    for i, element in enumerate(seq):
        if x <= element:  # Return the index of the first element >= x
            return i
    return len(seq)  # If no such element is found, return the length of the sequence