def search(x, seq):
    counter = 0
    if not seq:  # Check for empty sequence (handles both [] and ())
        return 0
    for element in seq:
        if x <= element:
            return counter
        counter += 1
    return counter  # Return length if x is greater than all elements