def search(x, seq):
    """ Takes in a value x and a sorted sequence seq, and returns the
    position that x should go to such that the sequence remains sorted """
    if not seq:
        return 0
    
    # If x is smaller than or equal to the first element, it goes at index 0
    if x <= seq[0]:
        return 0
    
    # If x is larger than the last element, it goes at the end
    if x > seq[-1]:
        return len(seq)
    
    # Search for the position between elements
    for i in range(len(seq) - 1):
        if seq[i] < x <= seq[i+1]:
            return i + 1
            
    return len(seq)