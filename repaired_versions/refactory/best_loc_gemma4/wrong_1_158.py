def search(x, seq):
    """ Takes in a value x and a sorted sequence seq, and returns the
    position that x should go to such that the sequence remains sorted """
    if not seq:
        return 0
    count = 0
    if x <= seq[0]:
        return 0
    elif x > seq[len(seq)-1]:
        return len(seq)
    else:
        while x > seq[count]:
            count += 1
        return count