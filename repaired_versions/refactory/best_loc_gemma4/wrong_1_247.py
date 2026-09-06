def search(x, seq):
    """
    Finds the index where x would be inserted into a sorted sequence 
    to maintain order, or the index of the first occurrence if it exists.
    Based on the test cases, it returns the number of elements in the 
    sequence that are strictly less than x.
    """
    position = 0
    for i in range(len(seq)):
        if seq[i] < x:
            position = i + 1
        else:
            break
    return position