def search(x, seq):
    """ Takes in a value x and a sorted sequence seq, and returns the
    position that x should go to such that the sequence remains sorted """
    if not seq:
        return 0
    elif len(seq) == 1:
        if x <= seq[0]:
            return 0
        else:
            return 1
    for i,j in enumerate(seq):
        if x < j:
            return i
        elif x == j:
            return i
        elif x > seq[len(seq)-1]:
            return len(seq)
        else:
            continue