def search(x, seq):
    counter = 0
    # Check if the sequence is empty (handles both lists and tuples)
    if not seq:
        return 0
    
    for element in seq:
        if x <= element:
            return counter
        counter += 1
        
    # If the loop finishes, x is greater than all elements in the sequence
    return counter