def search(x, seq):
    """ Takes in a value x and a sorted sequence seq, and returns the
    position that x should go to such that the sequence remains sorted """
    if not seq:
        return 0
    
    for i, element in enumerate(seq):
        if x <= element:
            return i
            
    return len(seq)