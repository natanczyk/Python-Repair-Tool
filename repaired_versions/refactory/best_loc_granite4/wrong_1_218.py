def search(x, seq):
    """ Takes in a value x and a sorted sequence seq, and returns the
    position that x should go to such that the sequence remains sorted """
    if not seq:  # Handles both empty lists and empty tuples
        return 0
    for i, elem in enumerate(seq):
        if x <= elem:
            return i
    return len(seq)  # Return the length if x is greater than all elements