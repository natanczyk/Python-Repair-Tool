def search(x, seq):
    if not seq:
        return 0
    
    i = 0
    while i < len(seq):
        if x <= seq[i]:
            return i
        i += 1
    
    return len(seq)
    """ Takes in a value x and a sorted sequence seq, and returns the
    position that x should go to such that the sequence remains sorted """