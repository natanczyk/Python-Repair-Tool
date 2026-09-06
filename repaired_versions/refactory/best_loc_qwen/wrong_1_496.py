def search(x, seq):
    """ Takes in a value x and a sorted sequence seq, and returns the
    position that x should go to such that the sequence remains sorted """
    length = len(seq)
    if length == 0:
        return 0
    for i, elem in enumerate(seq):
        if x <= elem:
            return i
    return length