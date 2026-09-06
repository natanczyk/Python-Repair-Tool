def search(x, seq):
    """ Takes in a value x and a sorted sequence seq, and returns the
    position that x should go to such that the sequence remains sorted """
    seq = tuple(seq)
    if x > seq[-1] if seq else False:
        return len(seq)
    else:
        i = 0
        while i < len(seq):
            if x <= seq[i]:
                return i
            i += 1
        return 0