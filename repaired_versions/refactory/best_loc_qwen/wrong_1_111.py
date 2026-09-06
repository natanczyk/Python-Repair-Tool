def search(x, seq):
    """ Takes in a value x and a sorted sequence seq, and returns the
    position that x should go to such that the sequence remains sorted """
    if seq == [] or seq == tuple():
        return 0
    
    for i, j in enumerate(seq):
        if x <= j:
            return i
    return len(seq)