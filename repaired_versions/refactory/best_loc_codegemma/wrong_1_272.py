def search(x, seq):
    """ Takes in a value x and a sorted sequence seq, and returns the
    position that x should go to such that the sequence remains sorted """
    if not seq:
        return 0
    elif x > max(seq):
        return len(seq)
    else:
        for i in range(len(seq)):
            if seq[i] >= x:
                return i
                break