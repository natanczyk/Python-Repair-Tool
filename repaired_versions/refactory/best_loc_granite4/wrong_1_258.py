def search(x, seq):
    """ Takes in a value x and a sorted sequence seq, and returns the
    position that x should go to such that the sequence remains sorted """
    res = len(seq)  # Initialize res to the length of the sequence
    for i, elem in enumerate(seq):
        if x <= elem:
            res = i
            break
    return res