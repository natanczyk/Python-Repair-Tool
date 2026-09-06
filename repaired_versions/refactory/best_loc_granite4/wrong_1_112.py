def search(x, seq):
    """ Takes in a value x and a sorted sequence seq, and returns the
    position that x should go to such that the sequence remains sorted """
    if not seq:  # Handle empty sequence
        return 0
    for i, j in enumerate(seq):
        if x <= j:
            return i
        if i == len(seq) - 1:  # If x is greater than all elements
            return len(seq)