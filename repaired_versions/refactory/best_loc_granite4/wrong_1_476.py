def search(x, seq):
    if not seq:  # Check if the sequence is empty
        return 0
    for i, element in enumerate(seq):
        if x <= element:  # Find the first element greater than or equal to x
            return i
    return len(seq)  # If x is greater than all elements, return the length of the sequence