def search(x, seq):
    """ Takes in a value x and a sorted sequence seq, and returns the
    position that x should go to such that the sequence remains sorted """
    largest=seq[0] if seq else None
    for i in range(len(seq)):
        if not seq:
            return 0 
        if x<=seq[i]:
            return i
        elif x>seq[len(seq)-1]:
            return len(seq)
    if not seq:
        return 0
    return len(seq)