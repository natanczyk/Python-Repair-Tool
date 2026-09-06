def search(x, seq):
    """ Takes in a value x and a sorted sequence seq, and returns the
    position that x should go to such that the sequence remains sorted """
    if not seq:
        return 0
    for i in range(len(seq)):
        if seq[i] < x:
            continue
        elif seq[i] > x:
            return i
        else:
            return i
    if x > seq[-1]:
        return len(seq)
    else:
        return 0