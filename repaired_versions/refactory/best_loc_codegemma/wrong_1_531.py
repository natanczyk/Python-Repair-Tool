def search(x, seq):
    """ Takes in a value x and a sorted sequence seq, and returns the
    position that x should go to such that the sequence remains sorted """
    counter = 0
    if len(seq) == 0:
        return 0
        
    for i in seq:
        if x > i:  # Fix: check if x is greater than i
            counter += 1
        else:
            return counter  # Fix: return counter only if x is not greater than i
            
    return counter