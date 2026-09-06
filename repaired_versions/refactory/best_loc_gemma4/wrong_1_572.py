def search(x, seq):
    """ Takes in a value x and a sorted sequence seq, and returns the
    position that x should go to such that the sequence remains sorted """
    if seq == []:
        return 0
    
    # To maintain sorted order and pass tests like search(5, [5, 5, 5]) == 0,
    # we need to find the first index i where seq[i] >= x.
    for i in range(len(seq)):
        if seq[i] >= x:
            return i
            
    # If x is greater than all elements in the sequence
    return len(seq)