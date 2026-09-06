def search(x, seq):
    """
    Finds the insertion index of x in a sorted sequence seq such that 
    the sequence remains sorted. This behaves like bisect_left.
    """
    i = 0
    while i < len(seq):
        if x <= seq[i]:
            return i
        i += 1
    return i