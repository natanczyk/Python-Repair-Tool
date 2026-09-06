def search(x, seq):
    counter = 0
    if not seq:  # Check if the sequence is empty
        return 0
    for element in seq:
        if x <= element:
            return counter
        counter += 1
    return len(seq)  # Return the length if x is greater than all elements