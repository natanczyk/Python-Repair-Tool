def search(x, seq):
    """ Takes in a value x and a sorted sequence seq, and returns the
    position that x should go to such that the sequence remains sorted """
    counter = -1
    if len(seq) == 0:
        return 0
    
    for i in seq:
        counter += 1
        if x <= i:
            return counter
    
    return counter + 1