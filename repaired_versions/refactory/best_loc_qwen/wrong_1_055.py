def search(x, seq):
    """ Takes in a value x and a sorted sequence seq, and returns the
    position that x should go to such that the sequence remains sorted """
    if not seq:
        return 0
    if x < seq[0]:
        return 0
    elif x > seq[-1]:
        return len(seq)
    counter = 0
    for i in seq:
        if x > i:
            counter += 1
        else:
            return counter
    return counter