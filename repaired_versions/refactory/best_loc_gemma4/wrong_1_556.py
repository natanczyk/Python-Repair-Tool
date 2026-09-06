def search(x, seq):
    """ Takes in a value x and a sorted sequence seq, and returns the
    position that x should go to such that the sequence remains sorted """
    if not seq:
        return 0
    
    # Since the sequence is already sorted, we just need to find the 
    # first index i where seq[i] >= x.
    for i in range(len(seq)):
        if seq[i] >= x:
            return i
            
    # If no element is >= x, it should be placed at the end of the sequence.
    return len(seq)