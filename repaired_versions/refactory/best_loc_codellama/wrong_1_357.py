def search(x, seq):
    """
    Takes in a value x and a sorted sequence seq, and returns the
    position that x should go to such that the sequence remains sorted
    """
    if type(seq) == tuple:
        new_seq = list(seq)
    else:
        new_seq = seq
    for i in range(len(new_seq)):
        if new_seq[i] < x:
            continue
        else:
            return i
    return len(new_seq)