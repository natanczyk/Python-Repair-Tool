def search(x, seq):
    """ Takes in a value x and a sorted sequence seq, and returns the
    position that x should go to such that the sequence remains sorted """
    if list(seq) == []:
        return 0
    for element in seq:
        if x <= element:
            return list(seq).index(element)
    if x >= max(seq):
        return len(seq)
    return len(seq) + 1