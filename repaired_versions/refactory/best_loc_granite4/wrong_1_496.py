def search(x, seq):
    """ Takes in a value x and a sorted sequence seq, and returns the
    position that x should go to such that the sequence remains sorted """
    if not seq:  # Handle empty sequence
        return 0
    length = len(seq)
    for i, elem in enumerate(seq):
        if x < elem:
            return i
        elif x == elem:
            return i
    return length  # x is greater than all elements, insert at the end