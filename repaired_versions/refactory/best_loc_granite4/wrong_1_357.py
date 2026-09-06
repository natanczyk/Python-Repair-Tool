def search(x, seq):
    """ Takes in a value x and a sorted sequence seq, and returns the
    position that x should go to such that the sequence remains sorted """
    if isinstance(seq, tuple):
        seq = list(seq)
    
    for i, val in enumerate(seq):
        if val >= x:  # Use >= to handle equal values
            return i
    return len(seq)