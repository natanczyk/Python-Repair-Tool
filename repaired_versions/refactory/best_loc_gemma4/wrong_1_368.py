def search(x, seq):
    """
    Finds the index where x is located in the sequence.
    If x is not present, it returns the index where x would be inserted 
    to maintain the sorted order of the sequence.
    """
    lst1 = list(seq)
    for i in range(len(lst1)):
        if lst1[i] >= x:
            return i
    return len(lst1)