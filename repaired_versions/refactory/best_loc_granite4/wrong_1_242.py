def search(x, seq):
    """ Takes in a value x and a sorted sequence seq, and returns the
    position that x should go to such that the sequence remains sorted """
    for i, val in enumerate(seq):
        if x <= val:  # Use <= to handle cases where x is equal to an element
            return i
    return len(seq)