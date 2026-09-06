def search(x, seq):
    """ Takes in a value x and a sorted sequence seq, and returns the
    position that x should go to such that the sequence remains sorted """
    # Handle empty sequence
    if len(seq) == 0:
        return 0
    
    # Check if x should go before the first element
    if x < seq[0]:
        return 0
    
    # Check if x should go after the last element
    if x > seq[len(seq) - 1]:
        return len(seq)
    
    # Search for the correct position
    for i, j in enumerate(seq):
        if x <= j:
            return i
    
    # If not found, append at the end
    return len(seq)