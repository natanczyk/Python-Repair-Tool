def search(x, seq):
    """ Takes in a value x and a sorted sequence seq, and returns the
    position that x should go to such that the sequence remains sorted """
    if not seq:  # Check for any empty sequence type
        return 0
    for i, value in enumerate(seq):
        if x <= value:
            return i
    return len(seq)