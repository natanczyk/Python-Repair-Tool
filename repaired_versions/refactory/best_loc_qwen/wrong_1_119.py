def search(x, seq):
    if seq == () or seq == []:
        return 0
    elif x < seq[0]:
        return 0
    else:
        for i, elem in enumerate(seq):
            if elem >= x:
                return i
        return len(seq)
    """ Takes in a value x and a sorted sequence seq, and returns the
    position that x should go to such that the sequence remains sorted """
    return