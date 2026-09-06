def search(x, seq):
    for i in range(len(seq)):
        if x == seq[i]:
            return i
        elif x < seq[0]:
            return 0
        elif i == len(seq) - 1 and x > seq[i]:
            return len(seq)
        elif x > seq[i] and x <= seq[i+1]:
            return i+1
    else:
        return len(seq)

    """ Takes in a value x and a sorted sequence seq, and returns the
    position that x should go to such that the sequence remains sorted """