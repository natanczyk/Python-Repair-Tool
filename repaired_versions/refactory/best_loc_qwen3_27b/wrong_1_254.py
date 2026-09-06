def search(x, seq):
    """
    Find the insertion index of x in a sorted sequence seq.
    This is equivalent to bisect_left.
    """
    i = 0
    while i < len(seq):
        if x <= seq[i]:
            return i
        i += 1
    return i