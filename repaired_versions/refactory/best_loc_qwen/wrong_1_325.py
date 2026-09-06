def search(x, seq):
    if not seq:
        return 0
    
    max_val = max(seq)
    for i, elem in enumerate(seq):
        if x <= elem:
            return i
    return len(seq)
    
    """ Takes in a value x and a sorted sequence seq, and returns the
    position that x should go to such that the sequence remains sorted """