def search(x, seq):
    """ Takes in a value x and a sorted sequence seq, and returns the
    position that x should go to such that the sequence remains sorted """
    if len(seq) == 0:
        return 0
    
    # The goal is to find the index of the first element that is >= x.
    # If x is greater than all elements, it should be placed at the end.
    if x > seq[-1]:
        return len(seq)
    
    for i, elem in enumerate(seq):
        if elem >= x:
            return i
            
    return len(seq)