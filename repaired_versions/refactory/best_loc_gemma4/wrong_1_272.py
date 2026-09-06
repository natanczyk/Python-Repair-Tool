def search(x, seq):
    """ Takes in a value x and a sorted sequence seq, and returns the
    position that x should go to such that the sequence remains sorted """
    if not seq:
        return 0
    
    enumerated = list(enumerate(seq))
    if x > max(seq):
        return len(seq)
    else:
        for i in range(len(enumerated)):
            if enumerated[i][1] >= x:
                return enumerated[i][0]