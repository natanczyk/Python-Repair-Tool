def search(val, seq):
    """ Takes in a value x and a sorted sequence seq, and returns the
    position that x should go to such that the sequence remains sorted """
    if not seq:
        return 0
    if val <= seq[0]:
        return 0
    elif val > seq[-1]:
        return len(seq)
    else:
        for i, item in enumerate(seq):
            if val <= item:
                return i
    return len(seq)